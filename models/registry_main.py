# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.tools.translate import _

class RegistryStage(models.Model):
    _name = 'registry.stage'
    _description = 'Stages of loans'

    name = fields.Char(string='Stage')

class RegistryMain(models.Model):
    _name = 'registry.main'
    _description = 'Project Opportunity Registry'
    _inherit = ['mail.thread','mail.activity.mixin']

    project_number=fields.Char(string='Project ID no.', copy=False, index=True, default=lambda self: _('New'), tracking=True)
    project_name = fields.Char(string='Project Name', required=True, tracking=True)
    project_description=fields.Text(string='Project Description', tracking=True)
    project_location=fields.Char(string='Project Location', required=True, tracking=True)
    project_owner=fields.Char(string='Project Owner', required=True, tracking=True)
    contact_person=fields.Char(string='Contact Person', required=True, tracking=True)
    meeting_schedule=fields.Date(string='Pre bid Meeting Schedule', tracking=True)
    stage = fields.Many2one('registry.stage', string="Stage", default=lambda self: self._default_stage(), tracking=True)
    reg_checklist = fields.One2many('registry.checklist', 'reg_check')


    @api.model
    def create(self, vals):
        if vals.get('project_number', 'New') == 'New':
            vals['project_number'] = self.env['ir.sequence'].next_by_code('project.registry.sequence') or 'New'
        return super(RegistryMain, self).create(vals)
    
    def _default_stage(self):
          stage = self.env['registry.stage'].search([('name', '=', 'New')], limit=1)
          return stage

