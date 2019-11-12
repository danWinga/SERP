import logging
from odoo import api, fields, models
from .. import exceptions
from odoo.exceptions import UserError, ValidationError
from openerp.exceptions import Warning

_logger = logging.getLogger(__name__)

class EventProduct(models.Model):
    """Adds Product to events."""
    _inherit = 'event.event'

    product_id = fields.Many2one('product.template', required=True, string='Product', track_visibillity='onchange',
                                 index=True,
                                 help="List available product to be linked with the event site visit")

