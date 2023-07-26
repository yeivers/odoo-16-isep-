# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    "name": "OpenEduCat Backend Theme",
    'description': """This module adds the feature of beautiful enterprise theme look
    to OpenEduCat. And good usability.""",
    "category": "Tools",
    "version": "16.0.1.0",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'company': 'OpenEduCat Inc.',
    "depends": ['base', 'web', 'mail'],
    "data": [
        'views/style.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'openeducat_backend_theme/static/src/scss/login.scss',
        ],
        'web.assets_backend_prod_only': [
            ('replace', 'web/static/src/main.js',
             'openeducat_backend_theme/static/src/js/edu/starter.js'
             ),
        ],
        'web.assets_backend': [
            'openeducat_backend_theme/static/src/scss/theme_primary_variables.scss',
            'openeducat_backend_theme/static/src/scss/edu/apps_menu.scss',
            'openeducat_backend_theme/static/src/scss/edu/common_style.scss',
            'openeducat_backend_theme/static/src/scss/edu/fields_extra.scss',
            'openeducat_backend_theme/static/src/scss/edu/form_view_extra.scss',
            'openeducat_backend_theme/static/src/scss/edu/list_view_extra.scss',
            'openeducat_backend_theme/static/src/scss/edu/navbar.scss',
            'openeducat_backend_theme/static/src/scss/edu/search_view_extra.scss',
            'openeducat_backend_theme/static/src/scss/edu/webclient_extra.scss',
            'openeducat_backend_theme/static/src/scss/kanban_view_mobile.scss',
            'openeducat_backend_theme/static/src/scss/search_view_mobile.scss',
            'openeducat_backend_theme/static/src/scss/search_view_extra.scss',
            'openeducat_backend_theme/static/src/scss/web_responsive.scss',
            'openeducat_backend_theme/static/src/js/edu/apps_menu.js',
            'openeducat_backend_theme/static/src/js/edu/web_client.js',
            # 'openeducat_backend_theme/static/src/js/edu/web_responsive.js',
            # 'openeducat_backend_theme/static/src/js/edu/kanban_renderer_mobile.js',
            'openeducat_backend_theme/static/src/js/edu/control_panel.js',
            'openeducat_backend_theme/static/src/js/edu/control_legacy_panel.js',
            'openeducat_backend_theme/static/src/js/edu/DropdownItem.js',
            'openeducat_backend_theme/static/src/js/edu/home_menu_wrapper.js',
            'openeducat_backend_theme/static/src/js/edu/home_menu.js',
            'openeducat_backend_theme/static/src/js/edu/search_panel.js',
            'openeducat_backend_theme/static/src/js/edu/user_menu.js',
            'openeducat_backend_theme/static/src/xml/menu.xml',
            'openeducat_backend_theme/static/src/scss/theme_primary_variables.scss',
        ],
        'web.assets_qweb': [
            'openeducat_backend_theme/static/src/xml/menu.xml',
        ],

        'web._assets_bootstrap': [
            'openeducat_backend_theme/static/src/scss/theme_primary_variables.scss',
            'openeducat_backend_theme/static/src/scss/edu/form_view_extra.scss',
        ],

        'web._assets_primary_variables': [
            '/openeducat_backend_theme/static/src/scss/theme_primary_variables.scss',
            # ('replace', '/web/static/src/legacy/scss/primary_variables.scss', '/openeducat_backend_theme/static/src/scss/theme_primary_variables.scss'),
        ],


    },
    'images': ['static/description/openeducat_backend_theme_banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
