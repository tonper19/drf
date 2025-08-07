from django.http import JsonResponse

def api_home(request, *args, **kwargs):
  body = request.body
  data = {}
  try:
    data = json.loads(body)
  except:
    pass
  print(data.keys())
  return JsonResponse({"message": "Hello, world! this is your Django API response (views.py)!"})
