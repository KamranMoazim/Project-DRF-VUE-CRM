from django.shortcuts import render

from rest_framework import viewsets
# Create your views here.

from .models import Lead

from .serializers import LeadSerizlizer


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerizlizer
    query_set = Lead.objects.all()

    def get_queryset(self):
        return self.query_set.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)