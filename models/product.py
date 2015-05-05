from openerp.osv import osv, fields


class ProductProduct(osv.osv):
    _inherit = 'product.product'

    _columns = {
	'default_code' : fields.char('SKU', select=True),
    }


class ProductTemplate(osv.osv):
    _inherit = 'product.template'

    _columns = {
        'upc': fields.char('UPC', select=True),
    }
