import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)

class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.library.doctor'
    _description = 'Doctor'

    name = fields.Char()
    gender = fields.Selection(
        selection=[('Male', 'Male'), ('Female', 'Female'), ])
    specialisation = fields.Char()
    category = fields.Char()
    age = fields.Integer()
    comment = fields.Text()
