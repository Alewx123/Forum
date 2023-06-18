from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    # Formular
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Help text dispare
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserUpdateForm(forms.ModelForm):
    # Formular
    class Meta:
        model = User
        fields = ['username', 'email']

    # Help text dispare
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args,**kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None

class ProfileUpdateForm(forms.ModelForm):
    #Imagine profil
    class Meta:
        model = ProfileModel
        fields = ['image']
