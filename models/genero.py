from odoo import models, fields

class Genero(models.Model):
    _name = 'biblioteca.genero'
    _description = 'Genero'


    name = fields.Char(string = "Nombre", required= True )
    color = fields.Char(string = "Color")