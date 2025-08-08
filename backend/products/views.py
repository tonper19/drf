from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'  # Optional, if you want to use a different field for lookup

# another way to define the view (instead of the class-based view above)
# This allows for easy reference in other parts of the application, such as URL patterns.
# It can be used in the urls.py file to create a URL pattern that maps to this
product_detail_view = ProductDetailAPIView.as_view()
