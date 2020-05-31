from django.contrib import admin
from .models import Products, Product_Price, Product_Photos

admin.site.register([Products,Product_Photos,Product_Price])

# Register your models here.
