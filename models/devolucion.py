from odoo import models, fields, api

class Devolucion(models.Model):
    _name = 'biblioteca.devolucion'
    _description = 'Devoluciones'

    name = fields.Char(string="Referencia", compute="_compute_name", store=True)
    fecha_devolucion = fields.Date(string = "Fecha devolucion", required= True )
    libro = fields.Many2many(comodel_name="biblioteca.libro", string="Libros", required=True)
    persona = fields.Many2one(comodel_name="biblioteca.usuario", string="Usuario", required=True)
    profesor = fields.Many2one(comodel_name="biblioteca.usuario", string="Encargado")

    libros_nombres = fields.Char(string="Títulos de libros", compute="_compute_libros_nombres", store=True)


    @api.depends('libro', 'persona')
    def _compute_name(self):
        for record in self:
            if record.libro and record.persona:
                libros_nombres = ", ".join(record.libro.mapped('name'))
                record.name = f"{libros_nombres} - {record.persona.name}"
            else:
                record.name = "Devolución sin completar"

    @api.depends('libro')
    def _compute_libros_nombres(self):
        for record in self:
            record.libros_nombres = ", ".join(record.libro.mapped('name'))

    @api.onchange('persona')
    def _onchange_persona(self):
        """Actualiza el dominio de los libros basándose en los préstamos del usuario seleccionado."""
        if self.persona:
            prestamos = self.env['biblioteca.prestamo'].search([
                ('persona', '=', self.persona.id),
                ('estado', '=', 'pendiente')
            ])
            libros_ids = prestamos.mapped('libro').ids
            return {'domain': {'libro': [('id', 'in', libros_ids)]}}
        else:
            return {'domain': {'libro': []}}

    @api.model
    def create(self, vals):
        devolucion = super(Devolucion, self).create(vals)
        for libro in devolucion.libro:
            prestamos = self.env['biblioteca.prestamo'].search([
                ('libro', '=', libro.id),
                ('persona', '=', devolucion.persona.id),  # Usar devolucion.persona.id
                ('estado', '=', 'pendiente')
            ])
            if prestamos:
                # Aumenta la cantidad del libro devuelto
                libro.cantidad += 1
                # Cambia el estado del préstamo a devuelto
                prestamos.write({'estado': 'devuelto'})
        return devolucion

