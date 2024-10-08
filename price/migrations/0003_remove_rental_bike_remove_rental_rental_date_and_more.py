# Generated by Django 5.1 on 2024-09-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_alter_bike_name_rental'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='bike',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='rental_date',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='rental_price',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='renter_email',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='renter_name',
        ),
        migrations.AddField(
            model_name='rental',
            name='bike_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rental',
            name='cust_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rental',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='rental',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='rental_type',
            field=models.CharField(choices=[('hourly', 'Per Hour'), ('daily', 'Per Day'), ('monthly', 'Per Month')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Bike',
        ),
    ]
