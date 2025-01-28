from odoo import models, fields, api


class prestamo(models.Model):
    _name = 'ModuloBibliotecaOdoo.prestamo'
    _description = 'ModuloBibliotecaOdoo.prestamo'

    fecha_inicio = fields.Date( string = "Fecha inicio", required = True )
    fecha_fin = fields.Date( string = "Fecha fin", required = True )
    # libro = fields.Many2one( comodel_name = "ModuloBibliotecaOdoo.libro", string = "Libro", required = True )
    persona = fields.Many2one( comodel_name = "ModuloBibliotecaOdoo.usuario", string = "Persona que pide el libro", required = True )
    profesor = fields.Many2one( comodel_name = "ModuloBibliotecaOdoo.usuario", string = "Persona que gestiona", required = True )

    
