from odoo import models, fields, api

class PropertyFeature(models.Model):
    _name = 'property.feature'
    _description = 'Property Feature'

    name = fields.Char('Name', required=True)
    category = fields.Selection([
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
        ('security', 'Security'),
        ('parking', 'Parking'),
        ('other', 'Other')
    ], string='Category', default='other')
    description = fields.Text('Description')
    property_count = fields.Integer(compute='_compute_property_count', string='Properties')

    @api.depends()
    def _compute_property_count(self):
        for record in self:
            record.property_count = self.env['real.estate.property'].search_count([
                ('feature_ids', 'in', record.id)
            ])