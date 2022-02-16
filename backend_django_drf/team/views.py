from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from .models import Team

from .serializers import TeamSerizlizer


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerizlizer
    query_set = Team.objects.all()

    def get_queryset(self):
        return self.query_set.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.save()


@api_view(["GET"])
def get_my_teams(request):
    team = Team.objects.filter(created_by=request.user).first()
    serializer = TeamSerizlizer(team)
    # print("get_my_teams ======> ", serializer.data)
    return Response(serializer.data)