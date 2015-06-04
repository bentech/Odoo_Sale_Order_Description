# -*- encoding: utf-8 -*-
from openerp import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    def product_id_change(self, *args, **kwargs):
        ret = super(SaleOrder, self).product_id_change(*args, **kwargs)
        cr = args[1]
        uid = args[2]
        ids = args[3]
        product_obj = self.pool.get('product.product')
        
        if not kwargs['flag']:
            if product_obj.description_sale:
                ret.value.name = '['+product_obj.default_code+'] '+product_obj.description_sale
            else:
                ret.value.name = self.pool.get('product.product').name_get(cr, uid, [product_obj.id], context=kwargs['context_partner'])[0][1]

        return ret