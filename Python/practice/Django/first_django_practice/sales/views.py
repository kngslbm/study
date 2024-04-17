from django.shortcuts import render, redirect
from .models import User, Sale


def index(request):
    sales = Sale.objects.all()
    context = {
        'sales': sales,
    }
    return render(request, 'index.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    sales = user.sale_set.all()
    context = {
        'user': user,
        'sales': sales,
    }
    return render(request, 'profile.html', context)


def detail(request, pk):
    sale = Sale.objects.get(pk=pk)
    context = {
        'sale': sale,
    }
    return render(request, 'detail.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    if request.method == 'POST':
        stuff = request.POST.get('stuff')
        price = request.POST.get('price')
        content = request.POST.get('content')
        user = request.user

        Sale.objects.create(stuff=stuff, price=price,
                            content=content, user=user)
        return redirect('index')
