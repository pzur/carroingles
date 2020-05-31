from rest_framework import serializers
from .models import Category
from apis_product.models import Products, Product_Photos, Product_Price


# Serializers define the API representation.
class CategoryALLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'photo')


class PriceProductsSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Product_Price
        fields = ['pricesale', 'pricesupplies', 'pricespecial']


class PhotosProductsSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Product_Photos
        fields = ['photo1', 'photo2', 'photo3', 'photo4']


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    list_price = PriceProductsSerializer(many=True, read_only=True)  # Padre
    product_photos =PhotosProductsSerializer(many=True, read_only=True)  # Padre

    class Meta:
        model = Products  # Hijo
        fields = ['id', 'product', 'feature', 'list_price', 'product_photos']


# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)  # Abuelo

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'products')
