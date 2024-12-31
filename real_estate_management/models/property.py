from odoo import models, fields, api

class Property(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char('Property Name', required=True)
    reference = fields.Char('Reference', readonly=True, copy=False)
    property_type_id = fields.Many2one('property.type', string='Property Type')
    address = fields.Char('Address', required=True, widget='google_maps_widget')
    latitude = fields.Float('Latitude')
    longitude = fields.Float('Longitude')
    price = fields.Float('Asking Price')
    area = fields.Float('Area (m²)')
    bedrooms = fields.Integer('Bedrooms')
    bathrooms = fields.Integer('Bathrooms')
    feature_ids = fields.Many2many('property.feature', string='Features')
    description = fields.Text('Description')
    state = fields.Selection([
        ('available', 'Available'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='Status', default='available')
    tour_ids = fields.One2many('property.tour', 'property_id', string='Property Tours')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['reference'] = self.env['ir.sequence'].next_by_code('real.estate.property')
        return super().create(vals_list)
    
    @api.model
    def _valid_field_parameter(self, field, name):
        return name == 'widget' or super()._valid_field_parameter(field, name)