from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserRegistrationForm, UserLoginForm
from users.models import CustomUser


class UserCreationView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('finance_app:home')
