# Generated by Django 4.1.6 on 2023-04-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0009_bill_customuser_renewal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bill",
            name="creditCardNumber",
            field=models.IntegerField(null=True),
        ),
    ]
