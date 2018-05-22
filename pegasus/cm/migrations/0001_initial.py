# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Archiv',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nummer', models.PositiveSmallIntegerField()),
                ('ticketid', models.PositiveIntegerField(default='')),
                ('auftraggeber', models.CharField(default='', max_length=100)),
                ('change', models.TextField()),
                ('datum', models.DateTimeField(blank=True, null=True)),
                ('techniker', models.ForeignKey(default='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveSmallIntegerField(default='')),
                ('prov', models.CharField(default='THIN', max_length=100, choices=[('Thin', 'Thin Provisioned'), ('Thick_LZ', 'Thick Lazy Zeroed'), ('Thick_EZ', 'Thick Eager Zeroed')])),
                ('location', models.CharField(default='withVM', max_length=50, choices=[('withVM', 'with VM'), ('separate', 'separate')])),
                ('node', models.CharField(default='0:0', max_length=100, choices=[('0:0', '0:0'), ('0:1', '0:1'), ('0:2', '0:2'), ('0:3', '0:3'), ('0:4', '0:4'), ('0:5', '0:5'), ('0:6', '0:6'), ('0:7', '0:7'), ('1:0', '1:0'), ('1:1', '1:1'), ('1:2', '1:2'), ('1:3', '1:3'), ('1:4', '1:4'), ('1:5', '1:5'), ('1:6', '1:6'), ('1:7', '1:7')])),
            ],
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('strasse', models.CharField(max_length=200)),
                ('hausnummer', models.PositiveSmallIntegerField()),
                ('ort', models.CharField(max_length=200)),
                ('plz', models.PositiveSmallIntegerField()),
                ('ansprechpartner', models.CharField(default='', max_length=200)),
                ('telefon', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=200)),
                ('fax', models.CharField(default='', max_length=20)),
                ('mks', models.PositiveIntegerField(default='999999')),
            ],
        ),
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kunde', models.ForeignKey(to='cm.Kunde')),
            ],
        ),
        migrations.CreateModel(
            name='Nic',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(default='', max_length=100)),
                ('vlanid', models.PositiveSmallIntegerField(default='')),
                ('adapter', models.CharField(default='vmxnet3', max_length=50, choices=[('vmxnet3', 'vmxnet3'), ('e1000', 'e1000'), ('e1000e', 'e1000e'), ('flexibel', 'flexibel')])),
            ],
        ),
        migrations.CreateModel(
            name='SCSI',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('adapter', models.CharField(default='pvscsi', max_length=50, choices=[('lsipar', 'LSI Logic Parallel'), ('lsisas', 'LSI Logic SAS'), ('pvscsi', 'Paravirtual SCSI')])),
            ],
        ),
        migrations.CreateModel(
            name='VM',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creationdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('beschreibung', models.CharField(default='', max_length=50)),
                ('inventory_location', models.CharField(default='', max_length=200)),
                ('datacenter_cluster', models.CharField(default='NUE', max_length=3, choices=[('PEG-RZ1+2', (('FKS', 'FKS'), ('NUE', 'NUE'))), ('PEG-RZ3', (('RST', 'RST'),)), ('PEG-RZ4', (('REG', 'REG'),))])),
                ('ressource_pool', models.CharField(default='', max_length=50)),
                ('storage', models.CharField(default='', max_length=100, choices=[('NUE', (('NUE-A', 'NUE-Tier-A'), ('NUE-B', 'NUE-Tier-B'), ('NUE-C', 'NUE-Tier-C'))), ('FKS', (('FKS-A', 'FKS-Tier-A'), ('FKS-B', 'FKS-Tier-B'), ('FKS-C', 'FKS-Tier-C'))), ('RST', (('RST-A', 'RST-Tier-A'), ('RST-B', 'RST-Tier-B'), ('RST-C', 'RST-Tier-C'))), ('REG', (('REG-A', 'REG-Tier-A'), ('REG-B', 'REG-Tier-B'), ('REG-C', 'REG-Tier-C')))])),
                ('vm_version', models.CharField(default='VMX-10', max_length=50, choices=[('VMX-08', 'VMX-08'), ('VMX-09', 'VMX-09'), ('VMX-10', 'VMX-10')])),
                ('os_version', models.CharField(default='WIN2K12R2', max_length=100, choices=[('WIN2K8', 'Windows Server 2008'), ('WIN2K8R2', 'Windows Server 2008 R2'), ('WIN2K12', 'Windows Server 2012'), ('WIN2K12R2', 'Windows Server 2012 R2'), ('LX-DEB8', 'Debian Linux 8'), ('LX-RH', 'RedHat Linux'), ('OTHER', 'Anderes OS')])),
                ('cpu', models.PositiveSmallIntegerField(default='1', choices=[(1, '1 vCPU  (1 socket,  1 core per socket)'), (2, '2 vCPUs (1 socket,  2 cores per socket)'), (4, '4 vCPUs (1 socket,  4 cores per socket)'), (8, '8 vCPUs (2 sockets, 4 cores per socket)')])),
                ('ram', models.PositiveSmallIntegerField(default=4)),
                ('kunde', models.ForeignKey(to='cm.Kunde')),
            ],
        ),
        migrations.AddField(
            model_name='scsi',
            name='vm',
            field=models.ForeignKey(to='cm.VM'),
        ),
        migrations.AddField(
            model_name='nic',
            name='vm',
            field=models.ForeignKey(to='cm.VM'),
        ),
        migrations.AddField(
            model_name='monitoring',
            name='vm',
            field=models.ForeignKey(to='cm.VM'),
        ),
        migrations.AddField(
            model_name='disk',
            name='scsi',
            field=models.ForeignKey(to='cm.SCSI'),
        ),
        migrations.AddField(
            model_name='change',
            name='vm',
            field=models.ForeignKey(to='cm.VM'),
        ),
        migrations.AddField(
            model_name='backup',
            name='kunde',
            field=models.ForeignKey(to='cm.Kunde'),
        ),
        migrations.AddField(
            model_name='backup',
            name='vm',
            field=models.ForeignKey(to='cm.VM'),
        ),
        migrations.AddField(
            model_name='archiv',
            name='vm',
            field=models.ForeignKey(to='cm.VM'),
        ),
    ]
