from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    create_ticket_from_crm_lead = fields.Boolean(
        string="Create helpdesk ticket from lead",
    )
    crm_stage_ids = fields.Many2many(
        string="CRM stages",
        comodel_name="crm.stage",
    )
