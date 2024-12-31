from odoo import models, fields, api
class TransportRoute(models.Model):
    _name = 'transport.route'
    _description = 'Transport Route'

    name = fields.Char(string='Route Name', required=True)
    route_line_ids = fields.One2many('transport.route.line', 'route_id', string='Route Lines')
    total_distance = fields.Float(string='Total Distance (KM)', compute='_compute_total_distance', store=True)
    total_time = fields.Float(string='Total Time (Hours)', compute='_compute_total_time', store=True)
    total_charges = fields.Float(string='Total Transport Charges', compute='_compute_total_charges', store=True)
    vehicle_id = fields.Many2one('transport.vehicle', string='Assigned Vehicle')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    @api.depends('route_line_ids.distance')
    def _compute_total_distance(self):
        for route in self:
            ordered_lines = route.route_line_ids.sorted('sequence')
            total = sum(line.distance for line in ordered_lines if line.distance)
            route.total_distance = round(total, 2)
    @api.depends('route_line_ids.time')
    def _compute_total_time(self):
        for route in self:
            route.total_time = sum(route.route_line_ids.mapped('time'))

    @api.depends('route_line_ids.transport_charges')
    def _compute_total_charges(self):
        for route in self:
            route.total_charges = sum(route.route_line_ids.mapped('transport_charges'))
            
    @api.model
    def action_confirm(self):
        self.ensure_one()
        self.write({'state': 'confirmed'})
        return True

    @api.model
    def action_start(self):
        self.ensure_one()
        self.write({'state': 'in_progress'})
        return True

    @api.model
    def action_done(self):
        self.ensure_one()
        self.write({'state': 'done'})
        return True

    @api.model
    def action_cancel(self):
        self.ensure_one()
        self.write({'state': 'cancelled'})
        return True

class TransportRouteLine(models.Model):
    _name = 'transport.route.line'
    _description = 'Transport Route Line'
    _order = 'sequence'

    sequence = fields.Integer(string='Sequence', default=10)
    route_id = fields.Many2one('transport.route', string='Route', required=True)
    source_location_id = fields.Many2one('transport.location', 
        string='Source Location', required=True)
    destination_location_id = fields.Many2one('transport.location', 
        string='Destination Location', required=True)
    distance = fields.Float(string='Distance (KM)')
    transport_charges = fields.Float(string='Transport Charges')
    time = fields.Float(string='Time (Hours)')

    # Computed fields for facilitating access to coordinates of source and destination locations
    source_location_latitude = fields.Float(
        related='source_location_id.latitude', 
        string='Source Latitude', 
        store=True,
        readonly=True)  # Agregamos readonly=True
    source_location_longitude = fields.Float(
        related='source_location_id.longitude', 
        string='Source Longitude', 
        store=True,
        readonly=True)
    destination_location_latitude = fields.Float(
        related='destination_location_id.latitude', 
        string='Destination Latitude', 
        store=True,
        readonly=True)
    destination_location_longitude = fields.Float(
        related='destination_location_id.longitude', 
        string='Destination Longitude', 
        store=True,
        readonly=True)

    @api.onchange('source_location_id', 'destination_location_id')
    def _onchange_locations(self):
        if self.source_location_id and self.destination_location_id:
            # Optional
            pass