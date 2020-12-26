# from odoo import http


# class IbeesWebsite(http.Controller):
#     @http.route('/ibees_website/ibees_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ibees_website/ibees_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ibees_website.listing', {
#             'root': '/ibees_website/ibees_website',
#             'objects': http.request.env['ibees_website.ibees_website'].search([]),
#         })

#     @http.route('/ibees_website/ibees_website/objects/<model("ibees_website.ibees_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ibees_website.object', {
#             'object': obj
#         })
