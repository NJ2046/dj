from django.http import HttpResponse


# noinspection PyUnusedLocal
def hello(request):
    return HttpResponse("hello world")


