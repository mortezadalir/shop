from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from products.models import ProductSort
from products.forms import UserForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http  import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.


class IndexView(TemplateView):
    template_name= 'products/index.html'

class ProductlistView(ListView):
    model= ProductSort


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_register(request):
    registered=False
    if request.method =="POST":
        user_form=UserForm(data=request.POST)




        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password) #  hasshing the Password
            user.save()

            registered=True
    #

    return render(request,'products/registration.html',{'forms':UserForm,
                                                             'registered':registered})

def user_login(request):

    if request.method=="POST":
        username=request.POST.get('login_username')
        password=request.POST.get('login_password')

        user=authenticate(username=username,password=password)
        print(user)

        if user:
            print(user.is_active)
            if user.is_active:
                print("helloo")
                login(request,user)
                return HttpResponseRedirect(reverse('index'))






    return render(request,'products/login.html')
