# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class Confirm_wizard(models.TransientModel):
    _name ='etudiant.wizard'

    idetudiantwizard = fields.Integer(string='Id etudiant à confirmer')

    @api.multi
    def confirm_dialog(self):
        student_id = self.env['etudiant.etudiant'].search([('id','=',self.idetudiantwizard)])
        if student_id:
            for stu in student_id:
                stu.confirm = True
