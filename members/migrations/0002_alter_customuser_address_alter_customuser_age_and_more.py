# Generated by Django 4.1.6 on 2023-04-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="address",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="age",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="phone",
            field=models.IntegerField(null=True),
        ),
    ]