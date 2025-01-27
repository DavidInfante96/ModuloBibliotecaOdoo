from odoo import models, fields

class Client(models.Model):
    _name = 'barbershop.client'
    _description = 'Client'

    #_inherit = 'res.users'

    name = fields.Char(string = "Nombre")
    phone = fields.Integer(string = "Teléfono")