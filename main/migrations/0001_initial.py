# Generated by Django 4.1.6 on 2023-03-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "email_address",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=10)),
            ],
        ),
    ]
