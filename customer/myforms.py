
from django import forms


class UserForm(forms.Form):
    username= forms.CharField(label = "USERNAME", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="PASSWORD", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="USERNAME", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label="PASSWORD", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label="CONFIRM", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label="EMAIL",
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    sex = forms.ChoiceField(label='GENDER', choices=gender)














