from odoo import models, fields, api


class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'biblioteca.prestamo'

    fecha_inicio = fields.Date( string = "Fecha inicio", required = True )
    fecha_fin = fields.Date( string = "Fecha fin", required = True )
    libro = fields.Many2one( comodel_name = "biblioteca.libro", string = "Libro", required = True )
    persona = fields.Many2one( comodel_name = "biblioteca.usuario", string = "Persona que pide el libro", required = True )
    profesor = fields.Many2one( comodel_name = "biblioteca.usuario", string = "Persona que gestiona", required = True )

    
