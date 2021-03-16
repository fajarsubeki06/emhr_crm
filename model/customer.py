from odoo import models, fields, api, _

class setting_web(models.Model):
    _name = 'emhr.customer'

    name = fields.Char('Name', required=True)
    img_customer = fields.Binary('Customer Pict', required=True)