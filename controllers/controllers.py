# -*- coding: utf-8 -*-
# from odoo import http


# class ReportDotMatrix(http.Controller):
#     @http.route('/report_dot_matrix/report_dot_matrix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_dot_matrix/report_dot_matrix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_dot_matrix.listing', {
#             'root': '/report_dot_matrix/report_dot_matrix',
#             'objects': http.request.env['report_dot_matrix.report_dot_matrix'].search([]),
#         })

#     @http.route('/report_dot_matrix/report_dot_matrix/objects/<model("report_dot_matrix.report_dot_matrix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_dot_matrix.object', {
#             'object': obj
#         })
