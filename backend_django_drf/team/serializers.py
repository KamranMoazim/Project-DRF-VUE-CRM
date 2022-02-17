from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Team

class UserSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )

class TeamSerizlizer(serializers.ModelSerializer):
    members = UserSerizlizer(many=True, read_only=True)
    created_by = UserSerizlizer(read_only=True)
    class Meta:
        model = Team

        fields = (
            'id',
            'name',
            'members',
            "created_by"
        )