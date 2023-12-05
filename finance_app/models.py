from django.db import models

from users.models import UserPosition


class FinancialOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компании')
    image = models.ImageField(upload_to='bank_images/', blank=True, null=True, verbose_name='Фото')
    bin = models.CharField(max_length=12, unique=True, verbose_name='БИН')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    active = models.BooleanField(default=True, verbose_name='Работает')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Финансовая организация'
        verbose_name_plural = 'Финансовые организации'


class Executive(models.Model):
    financial_organization = models.ForeignKey(to=FinancialOrganization, on_delete=models.CASCADE, verbose_name='Фин.организация')
    image = models.ImageField(upload_to='executive_images/', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    iin = models.CharField(max_length=12, unique=True, verbose_name='ИИН')
    position = models.ForeignKey(to=UserPosition, on_delete=models.PROTECT, verbose_name='Позиция')
    contact_phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    contact_email = models.EmailField(verbose_name='Email')
    start_date = models.DateField(verbose_name='Начало работы')
    end_date = models.DateField(null=True, blank=True, verbose_name='Конец работы')

    def __str__(self):
        return f'{self.financial_organization} | {self.full_name} | {self.position} | {self.start_date} - {self.end_date}'

    class Meta:
        verbose_name = 'Руководящее лицо'
        verbose_name_plural = 'Руководящие лица'