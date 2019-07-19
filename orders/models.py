from django.db import models
from django.db.models.signals import post_save

from products.models import Product





class Order(models.Model):
    person_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    comments = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=100, null=True, blank=True, decimal_places=2)

    def __str__(self):
        return 'Order №{}'.format(self.id)




class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=100, null=True, blank=True, decimal_places=2)

    def save(self, *args, **kwargs):
        prod_price = self.product.price
        tot_price = prod_price * self.quantity
        self.total_price = tot_price

        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, **kwargs):
    zakaz = instance.order
    products = ProductInOrder.objects.filter(order=zakaz)

    order_total_price = 0
    for prod in products:
        order_total_price += prod.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender = ProductInOrder)
