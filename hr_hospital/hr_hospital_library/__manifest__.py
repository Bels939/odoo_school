{
    'name': 'HR_Hospital',
    'summary': '123',
    'author': 'Sergey Bielik',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.1.2.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [

        'security/ir.model.access.csv',

        'views/hr_hospital_library_menu.xml',
        'views/hr_hospital_library_doctor_views.xml',
        'views/hr_hospital_library_diseases_views.xml',
        'views/hr_hospital_library_patient_views.xml',
        'views/hr_hospital_library_visits_views.xml',
    ],
    'demo': [
        'data/hr_hospital_diseases_data.xml',
        'demo/hr_hospital_doctor_demo.xml',
        'demo/hr_hospital_patient_demo.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
         # 'static/icon.png'
    ],

}
