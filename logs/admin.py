from django.contrib import admin
from .models import SystemApp, Incident, Account, Session


class SystemAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(SystemApp, SystemAppAdmin)


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem', 'incident_status')


admin.site.register(Incident, IncidentAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'roles',)


admin.site.register(Account, AccountAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('token', 'payload',)


admin.site.register(Session, SessionAdmin)
