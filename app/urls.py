from django.urls import path, include

from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'wins', views.WinViewSet)
router.register(r'losses', views.LossViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

