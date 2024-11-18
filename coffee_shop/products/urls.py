from django.urls import path
from .views import ProductFormView, ProductCreateAPIView, SuccessView, ProductListAPI

urlpatterns = [
    path("api/", ProductListAPI.as_view(), name="list_product_api"),
    path("agregar/", ProductFormView.as_view(), name="add_producto"),
    path("lista/", SuccessView.as_view(), name="list_product"),
    path("apiAdd/", ProductCreateAPIView.as_view(), name="add_product_api"),
]
