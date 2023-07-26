
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################
import base64
from odoo.http import Controller, request, route
from werkzeug.utils import redirect
DEFAULT_IMAGE = \
    '/openeducat_backend_theme/static/src/img/application-switcher-bg-dark.png'


class DashboardBackground(Controller):

    @route(['/app-menu-logo'], type='http', auth='user', website=False)
    def dashboard(self, **post):
        user = request.env.user
        company = user.company_id
        if company.logo:
            image = base64.b64decode(company.logo)
        else:
            return redirect(DEFAULT_IMAGE)

        return request.make_response(
            image, [('Content-Type', 'image')])
        
    @route('/theme/get/menus', type='json', auth='user')
    def get_theme_menus(self, **post):
        return request.env['ir.ui.menu'].sudo().load_menus_root()
