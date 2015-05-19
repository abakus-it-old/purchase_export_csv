from openerp import models, fields, api

class purchase_order_form(models.Model):
    _inherit = ['purchase.order']

    export_csv = fields.Text() #, compute='_create_export_csv')

    #@api.one
    #@api.onchange('order_line')
    @api.multi
    def create_export_csv(self):
        cr = self.env.cr
        uid = self.env.user.id
        purchase_order_line_obj = self.pool.get('purchase.order.line')
        purchase_order_lines = purchase_order_line_obj.search(cr, uid, [('order_id', '=', self.id)])
        if purchase_order_lines:
            text = ""
            for purchase_order_line in purchase_order_line_obj.browse(cr, uid, purchase_order_lines):
                reference = purchase_order_line.product_id.code

                #if reference == false:
                #    # get the supplier ref code
                #    suppliers_obj = self.pool.get('product.supplierinfo')
                #    suppliers = supplier_obj.search(cr, uid, [('product_tmpl_id', '=', purchase_order_line.product_id.product_tmpl_id)]):
                #    for supp in suppliers_obj.browse(cr, uid, suppliers):
                #        if supp.name == self.partner_id:
                #            reference = supp.product_code

                if reference:
                    text += str(internal_reference) + ", " + str(purchase_order_line.product_qty) + "\r\n"
            if self.export_csv != text:
                self.export_csv = text;
        else:
            if self.export_csv != "":
                self.export_csv = ""
