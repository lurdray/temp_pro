
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("template/", include("template.urls")),
    path("app-user/", include("app_user.urls")),
]
