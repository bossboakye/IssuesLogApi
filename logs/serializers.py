from rest_framework import serializers
from .models import Incident, SystemApp, Account, Session


class SystemAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SystemApp
        fields = ('created_at', 'name', 'updated_at')


class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incident
        fields = ('created_at', 'problem', 'incident_time', 'domain', 'severity', 'incident_status', 'root_cause',
                  'time_of_resolution', 'logged_by'
                  )


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('created_at', 'updated_at', 'first_name', 'last_name', 'email', 'password', 'remember_token', 'roles')


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('token', 'payload')
