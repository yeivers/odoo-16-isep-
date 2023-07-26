# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, models
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route('/openeducat_core_enterprise/'
                'openeducat_core_enterprise_onboarding_panel',
                auth='user', type='json')
    def openeducat_core_enterprise_onboarding_panel(self):
        """ Returns the `banner` for the sale onboarding panel.
            It can be empty if the user has closed it or if he doesn't have
            the permission to see it. """

        company = request.env.user.company_id
        if not request.env.user._is_admin() or \
                company.openeducat_core_onboard_panel == 'closed':
            return {}
        return {
            'html':
                request.env['ir.qweb']._render(
                    'openeducat_core_enterprise.'
                    'openeducat_core_enterprise_onboarding_panel',
                    {'company': company,
                     'state': company.update_core_onboarding_state()})
        }

# class CoreRender(models.Model):
#     _inherit = "ir.ui.view"
#
#     def _render(self, values=None, engine='ir.qweb', minimal_qcontext=False):
#         """ Render the template. If website is enabled on request,
#          then extend rendering context with website values. """
#         if request and getattr(request, 'is_frontend', False):
#             if request.website is None:
#                 request.website = self.env["website"].sudo().search([])[0]
#         return super(CoreRender, self). \
#             _render(values, engine=engine, minimal_qcontext=minimal_qcontext)
