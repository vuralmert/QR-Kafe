from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import LoginView, LogoutView, SignupView

urlpatterns = [
    path('login/', LoginView, name="Login"),
    path('logout/', LogoutView, name="Logout"),
    path('signup/', SignupView, name="Signup"),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),
]