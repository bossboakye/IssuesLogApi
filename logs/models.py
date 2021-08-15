from django.db import models


# from sqlalchemy import null


class SystemApp(models.Model):
    """List of all apps/services under monitoring"""
    uuid = models.IntegerField
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Incident(models.Model):
    """Incidents that are going to be logged"""
    Domain = models.TextChoices('Domain', 'Hubtel Third_Party')
    Severity = models.TextChoices('Severity', 'Minor, Major, Critical')
    IncidentStatus = models.TextChoices('IncidentStatus', 'Pending Resolved')
    system_app = models.ForeignKey(SystemApp, on_delete=models.RESTRICT)
    domain = models.CharField(blank=False, choices=Domain.choices, max_length=20)
    problem = models.TextField(blank=False, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    incident_time = models.DateTimeField(blank=False)
    severity = models.CharField(blank=False, choices=Severity.choices, max_length=20)
    systemapp_id = SystemApp.uuid
    incident_status = models.CharField(blank=False, choices=IncidentStatus.choices, max_length=20)
    root_cause = models.TextField(blank=True, max_length=300)
    logged_by = models.CharField(blank=False, max_length=50)
    time_of_resolution = models.DateTimeField(null=True, blank=True)
    duration = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.problem[:40]}..."


class Account(models.Model):
    """User Accounts Table"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(max_length=300, blank=False, unique=True)
    password = models.CharField(max_length=18, blank=False)
    Roles = models.TextChoices('Permission', 'Admin User SuperUser')
    roles = models.CharField(blank=False, choices=Roles.choices, max_length=10)
    remember_token = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Session(models.Model):
    """User Sessions Table"""
    token = models.CharField(max_length=100)
    payload = models.JSONField(max_length=100)

    def __str__(self):
        return self.token
