from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    helpdesk_ticket_ids = fields.One2many(
        comodel_name="helpdesk.ticket",
        inverse_name="sale_order_id",
        string="Helpdesk tickets",
        required=False,
    )
    helpdesk_ticket_count = fields.Integer(
        compute="_compute_helpdesk_ticket_count",
        string='Helpdesk ticket count',
        copy=False,
        default=0,
        store=True
    )
    create_ticket_from_sale_order = fields.Boolean(
        string="Create helpdesk ticket from sale order",
        related='company_id.create_ticket_from_sale_order',
    )
    allow_to_create_ticket_on_unconfirmed_orders = fields.Boolean(
        string="Allow to create ticket on unconfirmed orders",
        related='company_id.allow_to_create_ticket_on_unconfirmed_orders',
    )

    @api.depends('helpdesk_ticket_ids')
    def _compute_helpdesk_ticket_count(self):
        self.helpdesk_ticket_count = len(self.helpdesk_ticket_ids)

    def action_view_helpdesk_ticket(self):
        '''
        This function returns an action that display existing helpdesk ticket of given helpdesk_ticket_ids.
        When only one found, show the helpdesk ticket immediately.
        '''
        action = self.env.ref('helpdesk.helpdesk_ticket_action_main_tree')
        result = action.read()[0]
        create_hepldesk_ticket = self.env.context.get('create_hepldesk_ticket', False)

        # override the context to get rid of the default filtering
        result['context'] = {
            'default_company_id': self.company_id.id,
            'default_sale_order_id': self.id,
            'default_name': self.name,
            'default_partner_id': self.partner_id.id,
        }
        # choose the view_mode accordingly
        if len(self.helpdesk_ticket_ids) > 1 and not create_hepldesk_ticket:
            result['domain'] = "[('id', 'in', " + str(self.helpdesk_ticket_ids.ids) + ")]"
        else:
            res = self.env.ref('helpdesk.helpdesk_ticket_view_form', False)
            form_view = [(res and res.id or False, 'form')]
            if 'views' in result:
                result['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                result['views'] = form_view
            if not create_hepldesk_ticket:
                result['res_id'] = self.helpdesk_ticket_ids.id or False
        return result
