from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("registro/", RegisterView.as_view(), name="register"),
]
