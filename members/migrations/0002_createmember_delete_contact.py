# Generated by Django 4.1.6 on 2023-03-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CreateMember",
            fields=[
                (
                    "email_address",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("member_id", models.IntegerField()),
                (
                    "account_standing",
                    models.CharField(
                        choices=[
                            ("GS", "Good Standing"),
                            ("FD", "Fees Due"),
                            ("FOD", "Fees Overdue"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Contact",
        ),
    ]