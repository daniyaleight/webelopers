from django.forms import ModelForm, TextInput, forms, Textarea

from webel.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'email', 'text']
        widgets = {'title': TextInput(attrs={'name': 'title', 'placeholder': 'عنوان'}),
                   'email': TextInput(attrs={'name': 'email', 'placeholder': 'ایمیل شما'}),
                   'text': Textarea(attrs={'name': 'text', 'placeholder': 'پیام'}),
                   }


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.<br>')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class EditProfile(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
