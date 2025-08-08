from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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

# Using a function-based view for demonstration purposes
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            instance = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(instance, many=False).data
            return Response(data)
        # If no pk is provided, return a list of products
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title', 'Default Title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)






