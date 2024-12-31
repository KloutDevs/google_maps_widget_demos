from odoo import models, fields, api

class TransportVehicle(models.Model):
    _name = 'transport.vehicle'
    _description = 'Transport Vehicle'

    name = fields.Char(string='Vehicle Name', required=True)
    vehicle_number = fields.Char(string='Vehicle Number', required=True)
    vehicle_type = fields.Selection([
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('car', 'Car')
    ], string='Vehicle Type', required=True)
    capacity = fields.Float(string='Capacity (Tons)')
    driver_id = fields.Many2one('res.partner', string='Driver', domain=[('is_driver', '=', True)])