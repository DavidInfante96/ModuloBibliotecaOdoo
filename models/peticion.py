from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Peticion(models.Model):
    _name = 'biblioteca.peticion'
    _description = 'biblioteca.usuario'

    usuario = fields.Many2one( comodel_name = "biblioteca.usuario", string = "Usuario", required = True )
    titulo = fields.Char( string = "Titulo del libro", required = True )
    nombre_autor = fields.Char( string = "Nombre autor" )

    @api.constrains( "titulo" )
    def libro_existente( self ):
        for record in self:
            if self.env["biblioteca.libro"].search( [( 'name', 'ilike', record.titulo )] ).read( ["name"] ):
                raise ValidationError( "El libro que pides ya existe en la biblioteca." )
