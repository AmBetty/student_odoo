# -*- coding: utf-8 -*-
from odoo.exceptions import UserError
from odoo import models, fields, _, api
from datetime import datetime

class Etudiant(models.Model):
    _name = 'etudiant.etudiant'

    name = fields.Char(string = 'Name', required=True)
    last_name = fields.Char(string = 'Last Name', required = True)
    date_of_birth = fields.Date(string = 'Date of Birth')
    gender = fields.Selection([('m', 'Male'), ('f', 'Female')])
    classe_id = fields.Many2one('classe.classe', string='Class')
    code_c = fields.Char(compute = 'code_compute', store = 'True', readonly = True)
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    state = fields.Selection([('passable', 'Passable'), ('bon', 'Bon'), ('tb', 'Très Bon')], default = 'bon',string='State')
    reference = fields.Char(string = 'Reference', required = True)
    mail = fields.Char(string="Mail")
    confirm = fields.Boolean(string="inscription confirmé")

    _sql_constraints = [
        ('name_unique', 'unique(reference)', "Le champs référence doit être unique !"),
    ]

    @api.depends('name', 'last_name', 'date_of_birth')
    def code_compute(self):
        self.code_c = (self.name or '')+''+(self.last_name or '')

    @api.constrains('start_date','end_date')
    def check_date_fields(self):
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                raise UserError(_('S\'il vous plaît vérifier la date de fin.'))

    def action_confirm(self):
        partner_exist = self.env['etudiant.etudiant'].search_count([('name','=',self.name)])
        if partner_exist > 1:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Ce nom existe déjà !!!',
                'res_model': 'etudiant.wizard',
                'view_type': 'form',
                'view_mode': 'form',
                'context': {'default_idetudiantwizard':self.id},
                'target': 'new',
            }
        else:
            self.confirm = True

    def action_passable(self):
        self.state = 'passable'

    def action_bon(self):
        self.state = 'bon'

    def action_tres_bon(self):
        self.state = 'tb'


class Classe(models.Model):
    _name = 'classe.classe'

    name = fields.Char(string = 'Class Name')
    etudiant_id = fields.One2many('etudiant.etudiant', 'classe_id', string='Etudiants')
    total_of_student = fields.Integer (compute = '_display_count')
    student_of_class = [].+
