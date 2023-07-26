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

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError,UserError
#from .moodle_service import MoodleLib
#from odoo.addons.isep_courses_adapt.models.moodle_service import MoodleLib 
import logging
logger = logging.getLogger(__name__)

class OpmoodleAdmissionWizard(models.TransientModel):
    _name= "moodle.admission.wizard"
    admission_id=fields.Many2one("op.admission",string="Admision")
    moodle_course_line_ids = fields.One2many(
        'op.moodle.courses.wizard', 'moodle_admission_wizard',string='Course lines')

    moodle_course_id = fields.Integer(string="Course id")
    course_name = fields.Char(string="Course name")
    selected = fields.Boolean(string="Select", default=False)

    @staticmethod
    def get_moodle_course_order(course):
        return course.get('sortorder')


    @api.model
    def default_get(self,vals):
        res=super(OpmoodleAdmissionWizard,self).default_get(vals)
        by_category=False
        admission_id=self.env['op.admission'].browse(self.env.context.get('active_id'))
        moodle_id=admission_id.company_id.get_credential()
        user_moodle = moodle_id.get_users_by_field('email', admission_id.email)
        courses_id = []
        courses_new=[]
        if len(user_moodle) > 0:
            student_courses = moodle_id.get_users_courses(user_moodle[0]['id'])
            for student_course in student_courses:
                courses_id.append(student_course.get('id'))
        ####
        if by_category==False:
            for df in moodle_id.moodle_modules_ids:
                if int(df.number_id) not in  courses_id:
                    courses_new.append((0,0,{
                        'moodle_course_id': int(df.number_id),
                        'course_name': df.name,
                        'selected': True
                    }))
            for ct in admission_id.course_id.op_category_id.moodle_category_ids:
                if int(ct.number_id) not in  courses_id:
                    courses_new.append((0,0,{
                        'moodle_course_id': int(ct.number_id),
                        'course_name': ct.name,
                        'selected': True
                    }))
            #moodle_courses.sort(key=self.get_moodle_course_order)
            for bt in admission_id.batch_id.op_batch_subject_rel_ids.sorted(key=lambda r: r.code):
                if int(bt.moodle_id) not in  courses_id:
                    courses_new.append((0,0,{
                        'moodle_course_id': int(bt.moodle_id),
                        'course_name': bt.subject_id.name,
                        'selected': False
                    }))
        if by_category==True:
            for categ in admission_id.course_id.moodle_category_ids:
                response = moodle_id.get_course_by_field(
                    field="category", value=int(categ.category_moodle_number))
                moodle_courses = response['courses']
                moodle_courses.sort(key=self.get_moodle_course_order)
                for i, mdl_course in enumerate(moodle_courses):
                    if int(mdl_course.get('id')) not in courses_id:
                        
                        courses_new.append((0,0,{
                            'moodle_course_id': mdl_course.get('id'),
                            'course_name': mdl_course.get('fullname'),
                            'selected': False
                        }))
        res.update({'admission_id':admission_id.id,'moodle_course_line_ids':courses_new})
        return res

    def enroll_student(self):
        course_moodle_ids=self.moodle_course_line_ids.filtered(lambda x:x.selected==True)
        if not course_moodle_ids:
            raise UserError("Seleccione un modulo a Matricular")
        self.admission_id.enroll_student_moodle(course_moodle_ids.mapped('moodle_course_id'))
        return True

class OpMoodleCoursesWizard(models.TransientModel):
    _name = "op.moodle.courses.wizard"
    _description = "Moodle Courses Wizard"

    moodle_admission_wizard = fields.Many2one('moodle.admission.wizard')
    #group_change_wizard = fields.Many2one('op.student.group.change.wizard')
    moodle_course_id = fields.Integer(string="Course id")
    course_name = fields.Char(string="Course name")
    selected = fields.Boolean(string="Select", default=False)