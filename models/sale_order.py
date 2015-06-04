# -*- encoding: utf-8 -*-
from openerp import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    def product_id_change_with_wh(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, warehouse_id=False, context=None):
        product_uom_obj = self.pool.get('product.uom')
        product_obj = self.pool.get('product.product')

        res = self.product_id_change(cr, uid, ids, pricelist, product, qty=qty,
            uom=False, qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,
            lang=lang, update_tax=update_tax, date_order=date_order, packaging=packaging, fiscal_position=fiscal_position, flag=flag, context=context)

        product_obj = product_obj.browse(cr, uid, product, context=context)
        
        if not flag:
            if product_obj.description_sale:
                res.value.name = '['+product_obj.default_code+'] '+product_obj.description_sale
            else:
                res.value.name = self.pool.get('product.product').name_get(cr, uid, [product_obj.id], context=context_partner)[0][1]

        return res