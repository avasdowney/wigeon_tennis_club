# Generated by Django 4.1.6 on 2023-04-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0020_alter_customuser_zip_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="did_pay",
        ),
        migrations.AddField(
            model_name="customuser",
            name="payment_flag",
            field=models.BooleanField(default=True),
        ),
    ]
