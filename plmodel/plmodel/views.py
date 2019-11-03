from django.shortcuts import render


def main(request):
    ctx = {'main_page': 'active'}
    return render(request, 'index.html', ctx)


def project(request):
    ctx = {'project_page': 'active'}
    return render(request, 'index.html', ctx)