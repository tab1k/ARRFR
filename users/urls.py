from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserCreationView.as_view(), name='registration'),
]