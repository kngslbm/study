from django.shortcuts import render


def index(request):
    context = {
        'name': 'slbm',
    }
    return render(request, 'index.html', context)
