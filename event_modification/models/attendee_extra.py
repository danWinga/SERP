import logging
from odoo import api, fields, models
from .. import exceptions
from odoo.exceptions import UserError, ValidationError
from openerp.exceptions import Warning


class EventProduct(models.Model):
    """Adds event Attendee  extra."""
    _inherit = 'event.registration'

    extraNumber = fields.Integer(
        "Extra Prerson",
        index=True,
    )
    extraNotes = fields.Text(
        "More Info",
        index=True,
    )
    project_id = fields.Many2one('product.template', required=True, string='Project', track_visibillity='onchange',
                                 index=True,
                                 help="List available projects to be linked with the event site visit")




