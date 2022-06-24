from odoo import models, fields, api


class Product(models.Model):
    _inherit = "product.template"
    is_session_product = fields.Boolean(string="Use Session Product",
                                        help="Check this box to use as Product for session fee",
                                        default=False)
