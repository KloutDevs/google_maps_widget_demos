{
    'name': 'Real Estate Management',
    'version': '1.0',
    'category': 'Sales/Real Estate',
    'summary': 'Manage real estate properties and viewings',
    'description': """
        Real Estate Management System with:
        - Property Management
        - Property Types
        - Property Features
        - Location Tracking
        - Property Tours Integration
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_type_views.xml',
        'views/property_feature_views.xml',
        'views/property_views.xml',
        'views/property_tour_views.xml',
        'views/menus.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'sequence': 1,
}