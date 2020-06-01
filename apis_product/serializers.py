from rest_framework import serializers
from .models import Products, Product_Price, Product_Photos



class PricesProductsSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Product_Price
        fields = ['pricesale', 'pricesupplies', 'pricespecial']


class PhotosProductsSerializer(serializers.ModelSerializer):  # Los Campos Hijos
    class Meta:
        model = Product_Photos
        fields = ['photo1', 'photo2', 'photo3', 'photo4']


# Serializers define the API representation.
class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    list_price = PricesProductsSerializer(many=True, read_only=True) #Hijo1
    product_photos = PhotosProductsSerializer(many=True, read_only=True)  #Hijo2

    class Meta:
        model = Products # padre
        fields = ['id', 'product', 'feature', 'list_price', 'product_photos']



class ProductsDetailSerializer(serializers.ModelSerializer):
    list_price = PricesProductsSerializer(many=True, read_only=True) #HIJO1
    product_photos = PhotosProductsSerializer(many=True, read_only=True)  #HIJO2


    class Meta:
        model = Products #PADRE
        fields = ['id', 'product', 'feature', 'description', 'category','list_price', 'product_photos']



# https://www.django-rest-framework.org/api-guide/generic-views/
