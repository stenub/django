from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Kunde, VM, Change, Nic, SCSI, Disk, Backup, Archiv, Monitoring

# Register your models here.

admin.site.register(Kunde, SimpleHistoryAdmin)
admin.site.register(VM, SimpleHistoryAdmin)
admin.site.register(Change, SimpleHistoryAdmin)
admin.site.register(Nic, SimpleHistoryAdmin)
admin.site.register(SCSI, SimpleHistoryAdmin)
admin.site.register(Disk, SimpleHistoryAdmin)
admin.site.register(Backup, SimpleHistoryAdmin)
admin.site.register(Archiv, SimpleHistoryAdmin)
admin.site.register(Monitoring, SimpleHistoryAdmin)
