from odoo import models, fields

class Barber(models.Model):
    _name = 'barbershop.barber'
    _description = 'barber'

    name = fields.Char(string = "Nombre")