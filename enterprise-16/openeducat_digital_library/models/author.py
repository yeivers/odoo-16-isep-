
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################
from odoo import models, fields


class OpDigitalLibraryCategory(models.Model):
    _name = 'op.digital.library.author'
    _description = 'Author Of Material'

    name = fields.Char(string="Name")
