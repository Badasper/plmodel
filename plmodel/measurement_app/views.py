from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('Hello, I am measurement!')
