# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IncidentSerializer, SystemAppSerializer, AccountSerializer, SessionSerializer
from .models import Incident, SystemApp, Account, Session


class SystemAppViewSet(viewsets.ModelViewSet):
    queryset = SystemApp.objects.all()
    serializer_class = SystemAppSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
