from odoo import models, fields, api


class SaleWizard(models.TransientModel):
    _name = "academy.sale.wizard"
    _description = "Wizard: Quick Sale Orders for Students"

    def _default_session(self):
        return self.env['academy.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one("academy.session",
                                 string="Session",
                                 required=True,
                                 default=_default_session)
    session_student_ids = fields.Many2many('res.partner',
                                           string="Students in Current Session",
                                           related='session_id.student_ids',
                                           help="These are the students currently in the Session"
                                           )
    student_ids = fields.Many2many('res.partner',
                                   string='Student for Sale Order')

    def create_sale_orders(self):
        session_product_id = self.env['product.product'].search(['domain_product', '=', True], limit=1)
        if session_product_id:
            for student in self.student_ids:
                order_id = self.env['sale.order'].create({
                    'partner_id': student.id,
                    'session_id': self.session_id,
                    'order_line': [(0, 0, {'product_id': session_product_id.id, 'price_unit': self.session_id.total_price})]
                })

"""(0, 0, values)
Creates a new record from the provided values. The variable values must be of type dictionary.
(1, id, values)
Updates the record with specified id with the value in the values.
(2, id)
Removes the record with specified id from the database.
(3, id)
Removes the record with specified id from the set, but not from the database.
(4, id)
Adds an existing record with specified id to the set.
(5)
Unlink all records from the set, like using the command “3” on every record explicitly.
(6,"""