
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

from odoo import fields, models


class OpCourseLevel(models.Model):
    _name = "op.course.level"
    _description = "Course Level"

    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=True)
