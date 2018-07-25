from django.contrib import admin
from store.models import Customer,Product, Cart, Category

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
