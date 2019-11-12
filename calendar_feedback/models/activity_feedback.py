import logging
from odoo import api, fields, models
from .. import exceptions

_logger = logging.getLogger(__name__)

class ActivityFeedback(models.Model):
    _inherit = 'calendar.event'

    feedback = fields.Text('Feedback', states={'done': [('readonly', True)]})
