from odoo import models, fields, api, _

class setting_web(models.Model):
    _name = 'emhr.web_setting'

    title_desc = fields.Char('Title Description', required=True)
    desc = fields.Text('Descriptions', required=True)
    img_front = fields.Binary('Image Front Website', required=True)
    video_url = fields.Char('Video Url : https://www.youtube.com/embed/')
