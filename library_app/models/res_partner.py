from odoo import fields, models


# reference: ODE book pages (190-192)
class Partner(models.Model):
    _inherit = "res.partner"

    published_book_ids = fields.One2many(
        comodel_name="library.book",
        inverse_name="publisher_id",
        string="Publisher Books")

    book_ids = fields.Many2many(
        comodel_name="library.book",
        string="Authored Books")
