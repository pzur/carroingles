from django.urls import path,include
from . import views
from rest_framework import routers
from . import views


app_name = "apis_category"
router = routers.DefaultRouter()
router.register('List_Category_Products', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('List_All_Categorys/', views.CategoryAllViewSet.as_view())

]


# "http://127.0.0.1:8000/apis_category/List_Category_Products/"
# "http://127.0.0.1:8000/apis_category/List_All_Categorys/"