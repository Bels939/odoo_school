import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.library.diseases'
    _description = 'Diseases'

    name = fields.Char()
    comment = fields.Text()
