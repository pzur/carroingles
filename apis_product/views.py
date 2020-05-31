from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer,ProductsDetailSerializer
from rest_framework.permissions import AllowAny


class ProductsListView(generics.ListAPIView): #Solo muestra el Listado de productos
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (AllowAny,)


class ProductDetailView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializer
    permission_classes = (AllowAny,)


#RESFULL  = model.modelviewset
#LISTAR = ListAPIView
#CREAR  = CreateAPIView
#ELIMINAR =DestroyAPIView
#ACTUALIZAR =UpdateAPIView
#LISTAR/CREAR = ListCreateAPIView
