from django.contrib import admin
from manager.models import Enterprise

class EnterpriseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Enterprise, EnterpriseAdmin)