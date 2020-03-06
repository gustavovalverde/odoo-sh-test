from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    create_ticket_from_crm_lead = fields.Boolean(
        string="Create helpdesk ticket from lead",
        related='company_id.create_ticket_from_crm_lead',
        readonly=False,
    )
    crm_stage_ids = fields.Many2many(
        string="CRM stages",
        comodel_name="crm.stage",
        related='company_id.crm_stage_ids',
        readonly=False
    )

