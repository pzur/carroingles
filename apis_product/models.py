from django.db import models
from apis_category.models import Category
from django.contrib.auth.models import User

class Products(models.Model):
    product = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    feature = models.CharField(max_length=20, blank=True, null=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    #proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,related_name="productsuser")

    def __str__(self):
        return self.product


class Ingredients(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="ingredients")
    protein = models.FloatField()
    carbohydrates = models.FloatField()

    def __str__(self):
        return self.product.product

class Product_Photos(models.Model):
    photo1 = models.ImageField(upload_to='Products/Fotos', null=True, blank=True)
    photo2 = models.ImageField(upload_to='Products/Fotos', null=True, blank=True)
    photo3 = models.ImageField(upload_to='Products/Fotos', null=True, blank=True)
    photo4 = models.ImageField(upload_to='Products/Fotos', null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_photos')
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product.product)


class Product_Price(models.Model):
    pricesupplies = models.DecimalField(max_digits=5, decimal_places=2)
    pricesale = models.DecimalField(max_digits=5, decimal_places=2)
    pricespecial = models.DecimalField(max_digits=5, decimal_places=2)
    products = models.ForeignKey(Products, on_delete=models.CASCADE,related_name='list_price')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.products.product + ' Price sale:' + str(self.pricesale) + ' Price special:' + str(
            self.pricespecial)

