from django.urls import path
from . import views

from rest_framework_simplejwt import views as jwt_views

app_name = "app_user"

urlpatterns = [
    
    path("register/", views.RegisterView, name="register"),
    path("login/", views.LoginView, name="login"),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]