import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalVisits(models.Model):
    _name = 'hr.hospital.library.visits'
    _description = 'Visits'

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.library.doctor',
        required=True,
    )
    patient_id = fields.Many2one(
        comodel_name='hr.hospital.library.patient',
        required=True,
    )
    diseases_id = fields.Many2one(
        comodel_name='hr.hospital.library.diseases',
        required=True,
    )
    visit_date = fields.Datetime(string='Visit date',
                                 default=fields.Datetime.now)
    comment = fields.Text()
