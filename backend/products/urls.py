from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    # Alternative way to use the view directly:
    # path('<int:pk>/', product_detail_view, name='product-detail'), 
]
# This file defines the URL patterns for the product detail view in the Django application.
# It includes a path that maps to the ProductDetailAPIView, which will handle requests for product_ids.
# The 'name' parameter allows for easy reference to this URL pattern in templates and other parts of the application.
# The '<>' placeholder is used to capture the product_id from the URL, which will be passed to the view for processing.
# This setup allows for a clean and organized way to handle product detail requests in the application.

