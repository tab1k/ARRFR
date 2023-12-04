from django.contrib.auth.models import AbstractUser
from django.db import models


class UserPosition(models.Model):
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    photo = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Мужской'), ('female', 'Женский'), ('other', 'Другой')],
                              blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    position = models.ForeignKey(to=UserPosition, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'