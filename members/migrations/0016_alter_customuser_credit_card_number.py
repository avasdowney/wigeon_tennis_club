# Generated by Django 4.1.6 on 2023-04-23 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0015_alter_customuser_total_due"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="credit_card_number",
            field=models.IntegerField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1000000000000000),
                    django.core.validators.MaxValueValidator(9999999999999999),
                ],
            ),
        ),
    ]
