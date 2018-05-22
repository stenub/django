from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

# Create your models here.

class Kunde(models.Model):
    name = models.CharField(max_length=200)
    strasse = models.CharField(max_length=200)
    hausnummer = models.PositiveSmallIntegerField()
    ort = models.CharField(max_length=200)
    plz = models.PositiveSmallIntegerField()
    ansprechpartner = models.CharField(max_length=200, default='')
    telefon =  models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=200, default='')
    fax = models.CharField(max_length=20, default='')
    mks = models.PositiveIntegerField(default='')
    history = HistoricalRecords()
    def __str__(self):
        return self.name



class VM(models.Model):
    DATACENTER_CHOICES = (
        ('PEG-RZ1+2', (
                    ('FKS', 'FKS'),
                    ('NUE', 'NUE'),
                  )
        ),
        ('PEG-RZ3', (
                    ('RST', 'RST'),
                  )
        ),
        ('PEG-RZ4', (
                    ('REG', 'REG'),
                  )
        )
    )


    STORAGE_CHOICES = (
        ('NUE', (
                ('NUE-A', 'NUE-Tier-A'),
                ('NUE-B', 'NUE-Tier-B'),
                ('NUE-C', 'NUE-Tier-C'),
            )
        ),
        ('FKS', (
                ('FKS-A', 'FKS-Tier-A'),
                ('FKS-B', 'FKS-Tier-B'),
                ('FKS-C', 'FKS-Tier-C'),
            )
        ),
        ('RST', (
                ('RST-A', 'RST-Tier-A'),
                ('RST-B', 'RST-Tier-B'),
                ('RST-C', 'RST-Tier-C'),
            )
        ),
        ('REG', (
                ('REG-A', 'REG-Tier-A'),
                ('REG-B', 'REG-Tier-B'),
                ('REG-C', 'REG-Tier-C'),
            )
        ),
    )

    VM_CHOICES = (
        ('VMX-08', 'VMX-08'),
        ('VMX-09', 'VMX-09'),
        ('VMX-10', 'VMX-10'),
    )

    OS_CHOICES = (
        ('WIN2K8', 'Windows Server 2008'),
        ('WIN2K8R2', 'Windows Server 2008 R2'),
        ('WIN2K12', 'Windows Server 2012'),
        ('WIN2K12R2', 'Windows Server 2012 R2'),
        ('LX-DEB8', 'Debian Linux 8'),
        ('LX-RH', 'RedHat Linux'),
        ('OTHER', 'Anderes OS'),
    )

    CPU_CHOICES = (
        (1, '1 vCPU  (1 socket,  1 core per socket)'),
        (2, '2 vCPUs (1 socket,  2 cores per socket)'),
        (4, '4 vCPUs (1 socket,  4 cores per socket)'),
        (8, '8 vCPUs (2 sockets, 4 cores per socket)'),
    )

    kunde = models.ForeignKey(Kunde)
    name = models.CharField(max_length=200)
    creationdate = models.DateTimeField(default=timezone.now)
    beschreibung = models.CharField(max_length=50, default='')
    inventory_location = models.CharField(max_length = 200, default = '')
    datacenter_cluster = models.CharField(max_length=3, choices=DATACENTER_CHOICES, default='NUE')
    ressource_pool = models.CharField(max_length=50, default='')
    storage = models.CharField(max_length=100, choices=STORAGE_CHOICES, default='')
    vm_version = models.CharField(max_length=50, choices=VM_CHOICES, default='VMX-10')
    os_version = models.CharField(max_length=100, choices=OS_CHOICES, default='WIN2K12R2')
    cpu = models.PositiveSmallIntegerField(choices=CPU_CHOICES, default='1')
    ram = models.PositiveSmallIntegerField(default=4)
    history = HistoricalRecords()

    def sichern(self):
        self.creationdate = timezone.now()
        self.save()

    def __str__(self):
        return self.name



class Nic(models.Model):

    ADAPTER_CHOICES = (
        ('vmxnet3', 'vmxnet3'),
        ('e1000', 'e1000'),
        ('e1000e', 'e1000e'),
        ('flexibel', 'flexibel'),
    )

    vm = models.ForeignKey(VM)
    network = models.CharField(max_length=100, default='')
    vlanid = models.PositiveSmallIntegerField(default='')
    adapter = models.CharField(max_length=50, choices=ADAPTER_CHOICES, default='vmxnet3')
    history = HistoricalRecords()

    def __str__(self):
        return str(self.vm) + " " + self.adapter + " " + self.network



class SCSI(models.Model):

    ADAPTER_CHOICES = (
        ('lsipar', 'LSI Logic Parallel'),
        ('lsisas', 'LSI Logic SAS'),
        ('pvscsi', 'Paravirtual SCSI'),
    )

    vm = models.ForeignKey(VM)
    adapter = models.CharField(max_length = 50, choices=ADAPTER_CHOICES, default='pvscsi')
    history = HistoricalRecords()

    def __str__(self):
        return str(self.vm) + " " + self.adapter




class Disk(models.Model):

    TYPE_CHOICES = (
        ('Thin', 'Thin Provisioned'),
        ('Thick_LZ', 'Thick Lazy Zeroed'),
        ('Thick_EZ', 'Thick Eager Zeroed'),
    )

    LOCATION_CHOICES = (
        ('withVM', 'with VM'),
        ('separate', 'separate'),
    )

    NODE_CHOICES = (
        ('0:0', '0:0'),
        ('0:1', '0:1'),
        ('0:2', '0:2'),
        ('0:3', '0:3'),
        ('0:4', '0:4'),
        ('0:5', '0:5'),
        ('0:6', '0:6'),
        ('0:7', '0:7'),
        ('1:0', '1:0'),
        ('1:1', '1:1'),
        ('1:2', '1:2'),
        ('1:3', '1:3'),
        ('1:4', '1:4'),
        ('1:5', '1:5'),
        ('1:6', '1:6'),
        ('1:7', '1:7'),
    )

    scsi = models.ForeignKey(SCSI)
    size = models.PositiveSmallIntegerField(default='')
    prov = models.CharField(max_length=100, choices=TYPE_CHOICES, default='THIN')
    location = models.CharField(max_length = 50, choices=LOCATION_CHOICES, default='withVM')
    node = models.CharField(max_length=100, choices=NODE_CHOICES, default='0:0')
    history = HistoricalRecords()

    def __str__(self):
        return str(self.scsi) + " " + self.node + " " + str(self.size)



class Change(models.Model):
    vm = models.ForeignKey(VM)
    nummer = models.PositiveSmallIntegerField()
    techniker = models.ForeignKey('auth.User', default='')
    ticketid = models.PositiveIntegerField(default='')
    auftraggeber = models.CharField(max_length=100, default='')
    change = models.TextField()
    datum = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def sichern(self):
        self.datum = timezone.now()
        self.nummer = nummer+1
        self.save()

    def __str__(self):
        return self.change


class Backup(models.Model):
    kunde = models.ForeignKey(Kunde)
    vm = models.ForeignKey(VM)
    name = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Archiv(models.Model):
    vm = models.ForeignKey(VM)
    name = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Monitoring(models.Model):
    vm = models.ForeignKey(VM)
    name = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
