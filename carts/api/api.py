from carts.models import Cart
from rest_framework.generics import ListAPIView

from django.http import Http404

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions

from .serializers import CartSerializer
from products.models import Product
from django.conf import settings

User = settings.AUTH_USER_MODEL

class CartListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CartSerializer
    def get_queryset(self, *args, **kwargs):
        qs = Cart.objects.get_cart_or_create_cart(request=self.request)
        for x in qs:
            print(x)
        return qs

class CartAddProducts(ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, ]
        
    def get_queryset(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        product_obj = Product.objects.get(slug=slug)
        qs = Product.objects.filter(slug=slug)

        cart_obj = Cart.objects.filter(user__email=request.user)
        if cart_obj.exists():
            qs_cart = cart_obj.first()
        else:
            qs_cart = Cart.objects.new(request=request)

        if product_obj.slug in [x.slug for x in qs]:
            qs_cart.products.add(product_obj)
        user_qs = Cart.objects.filter(user=request.user)
        return user_qs

class CartRemoveProducts(ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    def get_queryset(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        product_obj = Product.objects.get(slug=slug)
        qs = Product.objects.filter(slug=slug)

        cart_obj = Cart.objects.filter(user__email=request.user)
        if cart_obj.exists():
            qs_cart = cart_obj.first()
        else:
            qs_cart = Cart.objects.new(request=request)

        if product_obj.slug in [x.slug for x in qs]:
            qs_cart.products.remove(product_obj)
        user_qs = Cart.objects.filter(user=request.user)
        return user_qs