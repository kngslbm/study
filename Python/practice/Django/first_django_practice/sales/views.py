from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Sale
from .forms import SaleForm, UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'sales/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'sales/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('index')


def userDelete(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            request.user.delete()
            auth_logout(request)

    return redirect('index')


def index(request):
    sales = Sale.objects.all()
    context = {
        'sales': sales,
    }
    return render(request, 'sales/index.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    sales = user.sale_set.all()
    context = {
        'user': user,
        'sales': sales,
    }
    return render(request, 'sales/profile.html', context)


def detail(request, pk):
    sale = Sale.objects.get(pk=pk)
    context = {
        'sale': sale,
    }
    return render(request, 'sales/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.user = request.user
            sale.save()
            return redirect('detail', sale.id)
        return redirect('index')
    else:
        form = SaleForm()

    context = {
        'form': form,
    }
    return render(request, 'sales/new.html', context)


def edit(request, pk):
    sale = Sale.objects.get(pk=pk)
    context = {
        'sale': sale,
    }
    return render(request, 'sales/edit.html', context)


def update(request, pk):
    if request.method == 'POST':
        sale = Sale.objects.get(pk=pk)
        sale.stuff = request.POST.get('stuff')
        sale.price = request.POST.get('price')
        sale.content = request.POST.get('content')
        sale.save()
        return redirect('detail', pk=sale.id)


def delete(request, pk):
    sale = Sale.objects.get(pk=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect('index')
    return redirect('detail', pk=sale.id)
