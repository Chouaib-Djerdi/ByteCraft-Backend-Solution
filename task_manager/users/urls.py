from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

urlpatterns = [
    # signup
    path("signup/", views.SignupView.as_view(), name="signup"),
    # login
    path("login/", views.LoginView.as_view(), name="login"),
    # logout
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # refresh token
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
