from django.shortcuts import render

from rest_framework import viewsets
# Create your views here.

from .models import Lead
from team.models import Team

from .serializers import LeadSerizlizer


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerizlizer
    query_set = Lead.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.query_set.filter(team=team, created_by=self.request.user)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team)