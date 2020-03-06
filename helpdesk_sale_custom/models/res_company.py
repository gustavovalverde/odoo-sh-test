from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    create_ticket_from_sale_order = fields.Boolean(
        string="Create helpdesk ticket from sale order",
    )
    allow_to_create_ticket_on_unconfirmed_orders = fields.Boolean(
        string="Allow to create ticket on unconfirmed orders",
    )
