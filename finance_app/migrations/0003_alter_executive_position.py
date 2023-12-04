# Generated by Django 5.0 on 2023-12-04 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance_app", "0002_alter_executive_options_and_more"),
        ("users", "0002_userposition_customuser_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="executive",
            name="position",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="users.userposition",
                verbose_name="Позиция",
            ),
        ),
    ]
