# Generated by Django 2.0.4 on 2018-04-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtbackup', '0005_auto_20180405_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='mgt_ip',
            field=models.GenericIPAddressField(default='0.0.0.0', protocol='IPv4'),
        ),
    ]