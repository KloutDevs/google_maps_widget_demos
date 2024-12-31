from odoo import models, fields, api

class PropertyType(models.Model):
    _name = 'property.type'
    _description = 'Property Type'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    description = fields.Text('Description')
    property_count = fields.Integer(compute='_compute_property_count', string='Properties')
    
    @api.depends()
    def _compute_property_count(self):
        for record in self:
            record.property_count = self.env['real.estate.property'].search_count([
                ('property_type_id', '=', record.id)
            ])