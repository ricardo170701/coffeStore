from rest_framework import serializers
from .models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        order_products_data = validated_data.pop("order_products")
        order = Order.objects.create(**validated_data)
        for order_product_data in order_products_data:
            OrderProduct.objects.create(order=order, **order_product_data)
        return order
