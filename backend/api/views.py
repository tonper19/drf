from products.models import Product
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request, *args, **kwargs):
  """
  DRF API View
  """
  model_data = Product.objects.all().order_by("?").first()
  data = {}
  if model_data:
    data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price'])
  return Response(data)
