from django.views.generic import DetailView, CreateView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderProductForm
from django.urls import reverse_lazy
from django.db.models import Sum, F
from decimal import Decimal


# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(user=self.request.user, is_active=True).first()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        order = self.get_object()
        total_price = (
            order.orderproduct_set.aggregate(
                total=Sum(F("product__price") * F("quantity"))
            )["total"]
            or 0
        )
        order_products = order.orderproduct_set.all().annotate(
            total=F("product__price") * F("quantity")
        )
        context["total_price"] = total_price
        context["total_price_with_tax"] = total_price * Decimal("1.12")
        context["order_products"] = order_products
        return context


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_orders")

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        quantity = self.request.POST.get("quantity", 1)
        form.instance.order = order
        form.instance.quantity = self.request.POST.get("quantity", 1)
        print(f"Cantidad recibida: {quantity}")
        form.save()
        return super().form_valid(form)
