from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    helpdesk_ticket_ids = fields.One2many(
        comodel_name="helpdesk.ticket",
        inverse_name="crm_lead_id",
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
    create_ticket_from_crm_lead = fields.Boolean(
        string="Create helpdesk ticket from lead",
        related='company_id.create_ticket_from_crm_lead',
    )
    crm_stage_helpdesk_ids = fields.Many2many(
        string="CRM stages",
        comodel_name="crm.stage",
        related='company_id.crm_stage_ids',
    )
    can_create_ticket_from_crm = fields.Boolean(
        string="Can create ticket from crm",
    )
    can_create_helpdesk_ticket = fields.Boolean(
        string="Can create ticket",
        compute="_compute_create_ticket"
    )

    @api.depends('crm_stage_helpdesk_ids', 'stage_id')
    def _compute_create_ticket(self):
        if self.stage_id.id in self.crm_stage_helpdesk_ids.ids:
            self.can_create_helpdesk_ticket = True
        else:
            self.can_create_helpdesk_ticket = False

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
            'default_crm_lead_id': self.id,
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
