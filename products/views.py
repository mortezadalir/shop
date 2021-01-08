from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from products.models import ProductSort
from products.forms import UserForm
from django.http import HttpResponse
from django.contrib.auth.models import User



# Create your views here.


class IndexView(TemplateView):
    template_name= 'products/index.html'

class ProductlistView(ListView):
    model= ProductSort

def user_register(request):
    registered=False
    if request.method =="POST":
        user_form=UserForm(data=request.POST)


        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password) #  hasshing the Password
            user.save()
    #

            registered=True;
    #

    return render(request,'products/registration.html',{'forms':UserForm,
                                                             'registered':registered})


#class ProductDetailView():
