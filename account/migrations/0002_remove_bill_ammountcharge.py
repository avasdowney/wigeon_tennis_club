# Generated by Django 4.1.6 on 2023-04-15 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bill",
            name="ammountCharge",
        ),
    ]
