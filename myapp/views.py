from django.http import HttpResponse

def my_endpoint(request):
    result = "Hello, this is my endpoint!"
    return HttpResponse(result)