# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectRegistry(http.Controller):
#     @http.route('/project_registry/project_registry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_registry/project_registry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_registry.listing', {
#             'root': '/project_registry/project_registry',
#             'objects': http.request.env['project_registry.project_registry'].search([]),
#         })

#     @http.route('/project_registry/project_registry/objects/<model("project_registry.project_registry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_registry.object', {
#             'object': obj
#         })
