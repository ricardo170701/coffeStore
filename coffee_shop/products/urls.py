from django.urls import path
from .views import ProductFormView, SuccessView

urlpatterns = [
    path("agregar/", ProductFormView.as_view(), name="add_product"),
    path("lista/", SuccessView.as_view(), name="list_product"),
]
