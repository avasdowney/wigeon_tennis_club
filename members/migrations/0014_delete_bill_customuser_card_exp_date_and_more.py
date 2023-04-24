# Generated by Django 4.1.6 on 2023-04-22 21:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0013_bill_total_due"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Bill",
        ),
        migrations.AddField(
            model_name="customuser",
            name="card_exp_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="credit_card_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="cvv",
            field=models.IntegerField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(100),
                    django.core.validators.MaxValueValidator(999),
                ],
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="zip_code",
            field=models.IntegerField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(10000),
                    django.core.validators.MaxValueValidator(99999),
                ],
            ),
        ),
    ]