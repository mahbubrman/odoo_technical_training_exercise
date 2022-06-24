from odoo import fields, api, models, exceptions


class Checkout(models.Model):
    _name = 'library.checkout'
    _description = "Checkout Request"

    member_id = fields.Many2one(
        "library.member",
        required=True)
    user_id = fields.Many2one(
        "res.users",
        "Librarian",
        default=lambda s: s.env.user)

    request_date = fields.Date(
        default=lambda s: fields.Date.today())

    line_ids = fields.One2many(
        "library.checkout.line",
        "checkout_id",
        string="Borrowed Books"
    )
    stage_id = fields.Many2one("library.checkout.stage",
                               default="_default_stage_id",
                               group_expand="_group_expand_stage_id"
                               )
    state = fields.Selection(related="state_id.state")

    checkout_date = fields.Date(readonly=True)
    close_date = fields.Date(reaonly=True)

    @api.model
    def _default_stage_id(self):
        stage = self.env["library.checkout.stage"]
        return stage.search([("state", "=", "new")], limit=1)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    @api.model
    def create(self, vals_list):
        # Code before create: should use the vals dict
        new_record = super().create(vals_list)
        # Code after create: can use the 'new record'
        # Created
        if new_record.stage_id.state in ("open", "close"):
            raise exceptions.UserError(
                "State not be allowed for new checkouts"
            )

        return new_record

    def write(self, vals):
        # Code before write: 'self' has old values
        if "stage_id" in vals:
            stage = self.env['library.checkout.stage']
            old_state = self.stage_id.state
            new_state = stage.browse(vals["stage_id"]).state
            if new_state != old_state and new_state == "open":
                vals['checkout_date'] = fields.Date.today()

            if new_state != old_state and new_state == "done":
                vals["close_date"] = fields.Date.today()

            super().write(vals)

            # Code after write: can use 'self' with the updated values

            return True

