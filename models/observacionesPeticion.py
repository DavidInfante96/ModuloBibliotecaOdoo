from odoo import models, fields, api
import re

class ObservacionesPeticion(models.Model):
    _inherit = 'biblioteca.peticion'

    observacion = fields.Text( string = "Observaciones" )
