from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="Lead",
        required=False,
    )

    def write(self, values):
        if (not self.env.user.has_group('crm_helpdesk_custom.group_can_create_ticket_from_crm') and not self.env.user.has_group('helpdesk_sale_custom.group_can_create_ticket_from_sale')) and not self.env.user.has_group('helpdesk.group_helpdesk_user'):
            raise UserError(_('You are not authorized to modify this document'))
        return super(HelpdeskTicket, self).write(values)

    @api.model
    def create(self, values):
        if (not self.env.user.has_group('crm_helpdesk_custom.group_can_create_ticket_from_crm') and not self.env.user.has_group('helpdesk_sale_custom.group_can_create_ticket_from_sale')) and not self.env.user.has_group('helpdesk.group_helpdesk_user'):
            raise UserError(_('You are not authorized to create this document'))
        return super(HelpdeskTicket, self).create(values)
