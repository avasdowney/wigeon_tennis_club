# Generated by Django 4.1.6 on 2023-04-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0012_rename_cardexpdate_bill_card_exp_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bill",
            name="total_due",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9999),
        ),
    ]
