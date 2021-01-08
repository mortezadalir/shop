from django import forms
from products.models import User

class   UserForm(forms.ModelForm):

    class Meta():
        model= User
        fields= ('username','password','email')
        widgets = {
        'password': forms.PasswordInput(),
    }
