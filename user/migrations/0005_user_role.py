# Generated by Django 5.1 on 2024-09-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_bikebooking_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('user', 'USER')], max_length=100, null=True),
        ),
    ]
