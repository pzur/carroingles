from django.urls import path,include
from . import views


app_name = "apis_user"



urlpatterns = [
    path('registeruser/', views.RegisterUsers.as_view()),
    path('authenticate/', views.LoginView.as_view()),

]


#endpoints

#http://127.0.0.1:8000/apis_user/registeruser/
#http://127.0.0.1:8000/apis_user/authenticate/