from django.urls import path
from . import views

app_name = "apis_product"

urlpatterns = [

    path('List_Products/', views.ProductsListView.as_view()),
    path('Detail_Products/<id>', views.ProductDetailView.as_view()),

]

# http://127.0.0.1:8000/apis_product/List_Products/
#http://127.0.0.1:8000/apis_product/Detail_Products/2