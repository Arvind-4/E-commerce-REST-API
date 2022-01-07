from carts.models import Cart
from django.http import HttpRequest

from products.models import Product

from products.api.serializers import ProductSerializer
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = (
            'user',
            'products',
            'subtotal',
            'total',
            'updated',
            'timestamp',
        )

    def get_products(self, obj):
        user = self.context.get('request').user
        results = Cart.objects.filter(user=user)
        for product in results:
            l = []
            l.append(product.products.all())
        product_list = l[0]
        products = product_list
        response = ProductSerializer(products, many=True).data
        return response