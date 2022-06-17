# -*- coding: utf-8 -*-
# from odoo import http


# class OdooAcademy(http.Controller):
#     @http.route('/odoo_academy/odoo_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_academy/odoo_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_academy.listing', {
#             'root': '/odoo_academy/odoo_academy',
#             'objects': http.request.env['odoo_academy.odoo_academy'].search([]),
#         })

#     @http.route('/odoo_academy/odoo_academy/objects/<model("odoo_academy.odoo_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_academy.object', {
#             'object': obj
#         })
