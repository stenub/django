# Generated by Django 2.0.3 on 2018-03-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtbackup', '0003_auto_20180328_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='mgt_ip',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4'),
        ),
    ]