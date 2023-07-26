# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'OpenEducat para ISEP',
    'version': '16.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 1,
    'summary': 'OpenEducat para ISEP',
    'complexity': "easy",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': ['openeducat_core','openeducat_exam','openeducat_admission'],
    'data': [
        'security/ir.model.access.csv',
        'data/plantillas_mail.xml',
        'data/ir_sequence_data.xml',
        'data/op_modality.xml',
        'wizard/wizard_certificate_report_view.xml',
        'wizard/courses_moodle_view.xml',
        'wizard/enroll_student_view.xml',
        'wizard/wizard_batch_view.xml',
        'views/category_view.xml',
        'views/course_view.xml',
        'views/student_view.xml',
        'views/moodle_view.xml',
        'views/company_view.xml',
        'views/sale_view.xml',
        'views/admision_view.xml',
        'views/modality.xml',
        'views/batch.xml',
        'views/subject_view.xml',
        'views/product_view.xml',
        'report/diploma_isep_latam_digital.xml',
        'report/certification_report_inherit.xml',
        'views/report_view.xml',
    ],
    'demo': [
    ],
    'css': [
    ],
    'qweb': [
       
    ],
    'js': [],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
        'website.assets_frontend': [
        ],
        'web.assets_backend': [
        ],
    },
}
