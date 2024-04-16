from django.shortcuts import render


def index(request):
    context = {
        'name': 'slbm',
    }
    return render(request, 'index.html', context)


def profile(request, username):
    context = {
        'username': username,
    }
    return render(request, 'profile.html', context)
