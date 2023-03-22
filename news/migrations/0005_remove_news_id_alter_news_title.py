# Generated by Django 4.1.6 on 2023-03-22 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_remove_news_email_news_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="id",
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.TextField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
