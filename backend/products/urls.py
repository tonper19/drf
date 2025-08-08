from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ProductCreateAPIView.as_view(), name='product-create'),
    path('', views.product_list_create_view), # <- Alternative way to use the view directly
    path('<int:pk>/', views.product_detail_view),
]

# function based views can be used directly in urlpatterns
# This is an alternative to using class-based views, which can be more verbose.
# urlpatterns = [
#     # path('', views.ProductCreateAPIView.as_view(), name='product-create'),
#     path('', views.product_alt_view), # <- Alternative way to use the view directly
#     path('<int:pk>/', views.product_alt_view),
# ]

