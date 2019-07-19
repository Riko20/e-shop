from django.contrib import admin
from orders.models import Order, ProductInOrder



class ProductInOrderAdmin(admin.TabularInline):
    model = ProductInOrder
    extra = 0




class OrderAdmin(admin.ModelAdmin):
    # list_display = ['name', 'email']
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderAdmin]
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)