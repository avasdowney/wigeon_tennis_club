from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest1EMail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest1FName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest1LName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest2EMail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest2FName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest2LName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest3EMail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest3FName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='courtreservationform',
            name='guest3LName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
