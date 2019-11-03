from django.shortcuts import render


def equipment(request):
    ctx = {'equipment_page': 'active'}
    return render(request, 'equipment_app/index.html', ctx)
