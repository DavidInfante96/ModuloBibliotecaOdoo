from odoo import models, fields, api

class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'biblioteca.prestamo'

    name = fields.Char(string="Referencia", compute="_compute_name", store=True)
    fecha_inicio = fields.Date( string = "Fecha inicio", required = True )
    fecha_fin = fields.Date( string = "Fecha fin", required = True )
    libro = fields.Many2one( comodel_name = "biblioteca.libro", string = "Libro", required = True )
    persona = fields.Many2one( comodel_name = "biblioteca.usuario", string = "Solicitante", required = True )
    profesor = fields.Many2one( comodel_name = "biblioteca.usuario", string = "Supervisor", required = True )

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('devuelto', 'Devuelto')
    ], string='Estado', default='pendiente')


    @api.depends('libro', 'persona')
    def _compute_name(self):
        for record in self:
            if record.libro and record.persona:
                record.name = f"{record.libro.name} - {record.persona.name}"
            else:
                record.name = "Préstamo sin completar"


    @api.model
    def create(self, vals):
        prestamo = super(Prestamo, self).create(vals)
        if prestamo.libro.cantidad <= 0:
            raise ValidationError(f"No hay existencias del libro '{prestamo.libro.name}' para hacer un préstamo.")
        prestamo.libro.cantidad -= 1  # Resta 1 a la cantidad del libro
        return prestamo

     
