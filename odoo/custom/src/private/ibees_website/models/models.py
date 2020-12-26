# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging

from odoo import _, api, fields, models
from odoo.exceptions import AccessError
from odoo.http import request
from odoo.osv import expression

logger = logging.getLogger(__name__)


class IbSeoMetadata(models.AbstractModel):

    _inherit = "website.seo.metadata"
    _description = "SEO metadata"

    # website_meta_description = fields.Html("Website meta description", translate=True)
