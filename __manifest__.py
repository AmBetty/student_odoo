# -*- coding: utf-8 -*-
{
'name' : 'Student Opération',
'version' : '10.0.2.0',
'author' : 'SYLVERSYS',
'description': """Gestion des étudiant, wizard """,
'depends': ['base', 'report'],
'data': [
'views/student.xml',
'wizard/confirm_wizard.xml',
],
'application': True,
'installable': True,
'auto_install': False,
}
