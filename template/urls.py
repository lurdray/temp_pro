from django.urls import path
from . import views

app_name = "template"

urlpatterns = [
    
    path("template/", views.TemplateView, name="template"),

]