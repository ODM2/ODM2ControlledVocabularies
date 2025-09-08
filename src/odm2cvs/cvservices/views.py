# view for health check
from django.http.response import HttpResponse

def health_check(request):
    return HttpResponse("OK")
