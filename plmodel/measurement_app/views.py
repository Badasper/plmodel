from django.shortcuts import render


def measurement(request):
    ctx = {'measurement_page': 'active'}
    return render(request, 'measurement_app/index.html', ctx)
