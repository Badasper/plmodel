from django.shortcuts import HttpResponse


def vendor(request):
    return HttpResponse('I am vendor!')
