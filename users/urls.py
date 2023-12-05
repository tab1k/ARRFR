from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('registration/', UserCreationView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
]