from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    create_ticket_from_sale_order = fields.Boolean(
        string="Create helpdesk ticket from sale order",
        related='company_id.create_ticket_from_sale_order',
        readonly=False,
    )
    allow_to_create_ticket_on_unconfirmed_orders = fields.Boolean(
        string="Allow to create ticket on unconfirmed orders",
        related='company_id.allow_to_create_ticket_on_unconfirmed_orders',
        readonly=False,
    )
