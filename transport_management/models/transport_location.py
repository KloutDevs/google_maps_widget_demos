# models/transport_location.py
from odoo import models, fields, api

class TransportLocation(models.Model):
    _name = 'transport.location'
    _description = 'Transport Location'

    name = fields.Char(string='Location Name', required=True)
    address = fields.Char(string='Address', required=True, default='')
    latitude = fields.Float(string='Latitude')
    longitude = fields.Float(string='Longitude')