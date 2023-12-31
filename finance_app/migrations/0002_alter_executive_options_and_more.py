# Generated by Django 5.0 on 2023-12-04 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="executive",
            options={
                "verbose_name": "Руководящее лицо",
                "verbose_name_plural": "Руководящие лица",
            },
        ),
        migrations.AlterField(
            model_name="executive",
            name="financial_organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="finance_app.financialorganization",
                verbose_name="Фин.организация",
            ),
        ),
        migrations.AlterField(
            model_name="executive",
            name="full_name",
            field=models.CharField(max_length=255, verbose_name="Полное имя"),
        ),
        migrations.AlterField(
            model_name="executive",
            name="iin",
            field=models.CharField(max_length=12, unique=True, verbose_name="ИИН"),
        ),
        migrations.AlterField(
            model_name="executive",
            name="position",
            field=models.CharField(max_length=255, verbose_name="Позиция"),
        ),
    ]
