
import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):
    _name = 'hr.hospital.library.patient'
    _description = 'Patient'

    name = fields.Char()
    gender = fields.Selection(
        selection=[('Male', 'Male'), ('Female', 'Female')]
    )
    diseases_id = fields.Many2one(
        comodel_name='hr.hospital.library.diseases',
        required=True,
    )
    adress = fields.Char()
    age = fields.Integer()
    comment = fields.Text()
