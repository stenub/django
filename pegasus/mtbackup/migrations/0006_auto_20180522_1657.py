# Generated by Django 2.0.3 on 2018-05-22 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbackup', '0005_auto_20180522_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='cust_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='cust_number',
            new_name='number',
        ),
    ]
