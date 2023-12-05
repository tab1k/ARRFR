from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg form-control-solid'}),
    )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'phone_number')

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid'}),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg form-control-solid'}),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg form-control-solid'}),
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid'}),
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid'}),
    )
    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid', 'placeholder': '8 (707) 777 77 77'}),
    )


class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'age')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg form-control-solid'
            self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-lg form-control-solid'
            self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg form-control-solid'
            self.fields['phone_number'].widget.attrs['class'] = 'form-control form-control-lg form-control-solid'
            self.fields['age'].widget.attrs['class'] = 'form-control form-control-lg form-control-solid'