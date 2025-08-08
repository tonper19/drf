from products.models import Product
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
  """
  DRF API View
  """
  instance = Product.objects.all().order_by("?").first()
  data = {}
  if instance:
    # data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price', 'sale_price'])
    data = ProductSerializer(instance).data
    
  return Response(data)
