# Generated by Django 4.1.6 on 2023-04-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0002_alter_customuser_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="phone",
            field=models.IntegerField(null=True),
        ),
    ]
