{
    'name': 'Transport Management',
    'version': '1.0',
    'category': 'Inventory/Transport',
    'summary': 'Manage transport routes and deliveries',
    'description': """
        Transport Management System with:
        - Transport Routes
        - Locations Management
        - Vehicle Management
        - Route Planning with Google Maps Integration
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/transport_route_views.xml',
        'views/transport_location_views.xml',
        'views/transport_vehicle_views.xml',
        'views/res_partner_views.xml',
        'views/menus.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
}