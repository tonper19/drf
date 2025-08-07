from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hello, world! this is your Django API response!"})
