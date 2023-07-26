# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat Student Skill Assessment',
    'version': '16.0.1.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Students Skill Assessments',
    'complexity': "easy",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_core_enterprise',
    ],
    'demo': ['demo/skill_category_demo.xml',
             'demo/skilll_demo.xml'],
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/skill_category_view.xml',
        'views/op_student_skill_assessment_view.xml',
        'views/op_student_skill_assessment_line_view.xml',
        'views/op_student_skill_view.xml',
        'views/op_student_skill_type_view.xml',
        'views/op_student_skill_level_view.xml',
        'views/op_student_skill_line.xml',
        'views/op_student_view.xml',
        'views/op_student_skill_name_view.xml',
        'views/op_student_skill_level_name_view.xml',
        'views/portal_student_skills.xml',
        'menu/menu.xml',
    ],
    'qweb': [],

    'images': [],
    'assets': {
        'web.assets_backend': [
            # '/openeducat_skill_enterprise/static/src/css/hr_skills.scss',
            '/openeducat_skill_enterprise/static/src/js/student_skills_widget.js',
            '/openeducat_skill_enterprise/static/src/js/list_renderer.js',
            '/openeducat_skill_enterprise/static/src/xml/skill_template.xml'
        ],
        'web.assets_qweb': [
            'openeducat_skill_enterprise/static/src/xml/*.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 208,
    'currency': 'EUR',
    'license': 'Other proprietary',
}
