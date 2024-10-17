from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}),
        label=''
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
        label=''
    )
    repeat_password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
        label=''
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Введите свой возраст'}),
        label='',
        max_value=999,
        min_value=0
    )
