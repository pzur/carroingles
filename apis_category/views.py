from django.shortcuts import render
from .models import Category
from django.http import Http404, response
from django.db import connection
from rest_framework import viewsets, decorators, parsers, status
from .serializers import CategorySerializer, CategoryALLSerializer
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import permissions


class CategoryAllViewSet(generics.ListAPIView):
    #permission_classes = (permissions.AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategoryALLSerializer
    permission_classes = (AllowAny,)


class CategoryViewSet(viewsets.ModelViewSet):  # Rest Full
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

