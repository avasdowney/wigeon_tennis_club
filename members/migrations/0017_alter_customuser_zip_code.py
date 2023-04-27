# Generated by Django 4.1.6 on 2023-04-24 01:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0016_alter_customuser_credit_card_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="zip_code",
            field=models.CharField(
                max_length=6,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9]{6}$", "Invalid postal code"
                    )
                ],
            ),
        ),
    ]