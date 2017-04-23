from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.template import loader

from .forms import RegistrationForm
from .models import Restaurant


def index(request):
    allRestaurant = Restaurant.objects.all()
    template = loader.get_template('restaurant/index.html')
    context = {
         'allRestaurant': allRestaurant,
    }
    return render(request,'restaurant/index.html',context)


def detail(request,Restaurant_id):
    template = loader.get_template('restaurant/details.html')
    allRestaurant = Restaurant.objects.filter(id=Restaurant_id)
    context= {
        'allRestaurant': allRestaurant,
    }
    return render(request,'restaurant/details.html',context)

def CustomerRegister(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'restaurant/index.html', {'form': form})
    context = {
        "form": form,
    }
    return render(request, 'restaurant/CustomerRegistration.html', context)
