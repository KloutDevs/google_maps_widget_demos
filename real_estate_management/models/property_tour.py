from odoo import models, fields, api

class PropertyTour(models.Model):
    _name = 'property.tour'
    _description = 'Property Tour'
    _order = 'tour_date desc, id desc'

    name = fields.Char(string='Tour Reference', required=True)
    property_id = fields.Many2one('real.estate.property', string='Property', required=True)
    tour_line_ids = fields.One2many('property.tour.line', 'tour_id', string='Tour Stops')
    tour_date = fields.Datetime('Tour Date')
    duration = fields.Float('Duration (hours)', compute='_compute_duration', store=True)
    total_distance = fields.Float('Total Distance (km)', compute='_compute_total_distance', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], string='Status', default='draft')

    @api.depends('tour_line_ids.time')
    def _compute_duration(self):
        for tour in self:
            tour.duration = sum(tour.tour_line_ids.mapped('time'))

    @api.depends('tour_line_ids.distance')
    def _compute_total_distance(self):
        for tour in self:
            total = sum(tour.tour_line_ids.mapped('distance'))
            tour.total_distance = round(total, 2)

class PropertyTourLine(models.Model):
    _name = 'property.tour.line'
    _description = 'Property Tour Line'
    _order = 'sequence'

    sequence = fields.Integer(string='Sequence', default=10)
    tour_id = fields.Many2one('property.tour', string='Tour', required=True)
    source_location_id = fields.Many2one('tour.location', 
        string='Source Location', required=True)
    destination_location_id = fields.Many2one('tour.location', 
        string='Destination Location', required=True)
    distance = fields.Float(string='Distance (KM)')
    time = fields.Float(string='Duration (Hours)')

    # Campos computados para coordenadas
    source_location_latitude = fields.Float(
        related='source_location_id.latitude',
        string='Source Latitude',
        store=True,
        readonly=True
    )
    source_location_longitude = fields.Float(
        related='source_location_id.longitude',
        string='Source Longitude',
        store=True,
        readonly=True
    )
    destination_location_latitude = fields.Float(
        related='destination_location_id.latitude',
        string='Destination Latitude',
        store=True,
        readonly=True
    )
    destination_location_longitude = fields.Float(
        related='destination_location_id.longitude',
        string='Destination Longitude',
        store=True,
        readonly=True
    )

class TourLocation(models.Model):
    _name = 'tour.location'
    _description = 'Tour Location'

    name = fields.Char('Location Name', required=True)
    address = fields.Char('Address', required=True, widget='google_maps_widget')
    latitude = fields.Float('Latitude')
    longitude = fields.Float('Longitude')
    
    @api.model
    def _valid_field_parameter(self, field, name):
        return name == 'widget' or super()._valid_field_parameter(field, name)