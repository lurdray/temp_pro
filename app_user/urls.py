from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [
    
    path("app-user/", views.AppUserView, name="app_user"),

]