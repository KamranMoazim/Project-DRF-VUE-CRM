from rest_framework import serializers

from .models import Lead

from team.serializers import UserSerizlizer

class LeadSerizlizer(serializers.ModelSerializer):
    assigned_to = UserSerizlizer(read_only=True)
    class Meta:
        model = Lead
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        )
        fields = (
            'id',
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'assigned_to',
            'created_at',
            'modified_at',
        )