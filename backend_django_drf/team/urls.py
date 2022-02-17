
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, get_my_teams, add_member_to_team

router = DefaultRouter()
router.register("teams", TeamViewSet, basename="teams")

urlpatterns = [
    path("teams/get-my-teams/", get_my_teams, name="get_my_teams"),
    path("teams/add-member-to-team/", add_member_to_team, name="add_member_to_team"),
    path("", include(router.urls)),
]
