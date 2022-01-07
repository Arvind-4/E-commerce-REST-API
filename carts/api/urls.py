from django.urls import path

from .api import (
    CartListView,
    CartAddProducts,
    CartRemoveProducts
)

urlpatterns = [
    path('', CartListView.as_view()),
    path('add/<str:slug>/', CartAddProducts.as_view()),
    path('remove/<str:slug>/', CartRemoveProducts.as_view()),
]