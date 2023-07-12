from odoo import models, fields, api

class RegistryDocType(models.Model):
    _name = 'registry.doctype'
    _description = 'Document Types'

    name = fields.Char(string='Document Type')

class RegistryDocStatus(models.Model):
    _name = 'registry.docstatus'
    _description = 'Document Status'

    name = fields.Char(string='Document Status')

class RegistryChecklist(models.Model):
    _name = 'registry.checklist'
    _description = 'Checklist for the POR'

    doc_type = fields.Many2one('registry.doctype', string='Document Type')
    doc_description=fields.Text(string='Document Description')
    doc_status=fields.Many2one('registry.docstatus', string='Document Status')
    reg_check = fields.Many2one('registry.main', string='Checklist')


