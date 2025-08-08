from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # This method is NOT, NOT fucking called when a new product is created
        # You can add custom logic here if needed, ONLY IF IT WORKS!
        print(serializer.validated_data)
        title = serializer.validated_data.get('title', 'Default Title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save()

# another way to define the view (instead of the class-based view above)
# This allows for easy reference in other parts of the application, such as URL patterns.
# It can be used in the urls.py file to create a URL pattern that maps to this
product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'  # Optional, if you want to use a different field for lookup

# another way to define the view (instead of the class-based view above)
# This allows for easy reference in other parts of the application, such as URL patterns.
# It can be used in the urls.py file to create a URL pattern that maps to this
product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    """
    Not used, instead we use ProductListCreateAPIView
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()







