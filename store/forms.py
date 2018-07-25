from django import forms
from store.models import Customer


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=25)
    password = forms.CharField(required=True, max_length=12, widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    verify_password = forms.CharField(label='Verify Password', widget=forms.PasswordInput())
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'verify_password']
        widgets = {
            'password': forms.PasswordInput()
        }
