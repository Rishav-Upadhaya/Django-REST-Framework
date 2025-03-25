from django.urls import path
from .views import *

urlpatterns = [
    # path('', ProductListAPIView.as_view(), name='product-create'),
    # path('', ProductCreateAPIView.as_view(), name='product-create'),
    path('', ProductListCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
]
