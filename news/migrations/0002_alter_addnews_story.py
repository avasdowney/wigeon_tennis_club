# Generated by Django 4.1.6 on 2023-04-12 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addnews",
            name="story",
            field=models.CharField(max_length=99999),
        ),
    ]
