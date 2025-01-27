# -*- coding: utf-8 -*-
# from odoo import http


# class Barbershop(http.Controller):
#     @http.route('/barbershop/barbershop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barbershop/barbershop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('barbershop.listing', {
#             'root': '/barbershop/barbershop',
#             'objects': http.request.env['barbershop.barbershop'].search([]),
#         })

#     @http.route('/barbershop/barbershop/objects/<model("barbershop.barbershop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barbershop.object', {
#             'object': obj
#         })
