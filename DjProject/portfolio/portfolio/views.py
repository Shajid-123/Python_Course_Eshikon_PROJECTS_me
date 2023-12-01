from django.http import HttpResponse

def demo(request):
    return HttpResponse("This is a root url function")