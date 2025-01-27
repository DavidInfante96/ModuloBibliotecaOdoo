from odoo import models, fields

class Appointment(models.Model):
    _name = 'barbershop.appointment'
    _description = 'Appointment'

    client = fields.Many2one(comodel_name = "barbershop.client", string = "Cliente")
    barber = fields.Many2one(comodel_name = "barbershop.barber", string = "Peluquero")

    ap_type = fields.Selection([("1", "Peluquería"),("2", "Estética")], string = "Tipo de cita")

    datetime = fields.Datetime(string = "Fecha y hora")

