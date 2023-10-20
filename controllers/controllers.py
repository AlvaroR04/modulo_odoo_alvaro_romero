# -*- coding: utf-8 -*-
# from odoo import http


# class AlvaroRomero(http.Controller):
#     @http.route('/alvaro_romero/alvaro_romero', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alvaro_romero/alvaro_romero/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alvaro_romero.listing', {
#             'root': '/alvaro_romero/alvaro_romero',
#             'objects': http.request.env['alvaro_romero.alvaro_romero'].search([]),
#         })

#     @http.route('/alvaro_romero/alvaro_romero/objects/<model("alvaro_romero.alvaro_romero"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alvaro_romero.object', {
#             'object': obj
#         })
