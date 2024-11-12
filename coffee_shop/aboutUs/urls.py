from django.urls import path
from . import views

urlpatterns = [
    path("informacion/", views.about_us, name="aboutUs"),
]
