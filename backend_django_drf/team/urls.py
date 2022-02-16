
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, get_my_teams

router = DefaultRouter()
router.register("teams", TeamViewSet, basename="teams")

urlpatterns = [
    path("teams/get-my-teams/", get_my_teams, name="get_my_teams"),
    path("", include(router.urls)),
]
