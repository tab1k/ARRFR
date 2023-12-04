from django.db import models

from users.models import UserPosition


class FinancialOrganization(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='bank_images/', blank=True, null=True)
    bin = models.CharField(max_length=12, unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)

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
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    start_date = models.DateField()  # Дата начала работы
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.financial_organization} | {self.full_name} | {self.position} | {self.start_date} - {self.end_date}'

    class Meta:
        verbose_name = 'Руководящее лицо'
        verbose_name_plural = 'Руководящие лица'