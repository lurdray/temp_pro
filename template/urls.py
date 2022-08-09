from django.urls import path
from . import views

app_name = "template"

urlpatterns = [
    
    path("add/", views.AddTemplateView, name="add_template"),
    path("all/", views.AllTemplateView, name="all_template"),
    path("get/<int:template_id>/", views.GetTemplateView, name="get_template"),
    path("update/<int:template_id>/", views.UpdateTemplateView, name="update_template"),
    path("delete/<int:template_id>/", views.DeleteTemplateView, name="delete_template"),

]