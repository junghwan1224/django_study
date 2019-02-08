from django import forms
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(UserCreationForm):

    email = forms.EmailField()
    address = forms.CharField(max_length=30)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None:
            raise forms.ValidationError('Please write your email')
        return email

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address is None:
            raise forms.ValidationError('Please write your address')
        return address

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()
        return user


class SignInForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'wrong id or password',
        'inactive': 'no user',
    }

###


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('phone', 'address',)


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)
