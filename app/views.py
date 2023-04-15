from django.shortcuts import render
from app.models import Team, Game, Win, Loss
from app.serializers import TeamSerializer, GameSerializer, WinSerializer, LossSerializer
from rest_framework import viewsets

# Create your views here.


class TeamViewSet(viewsets.ModelViewSet):  # new
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class GameViewSet(viewsets.ModelViewSet):  # new
    queryset = Game.objects.all()
    serializer_class = GameSerializer



class WinViewSet(viewsets.ModelViewSet):  # new
    queryset = Win.objects.all()
    serializer_class = WinSerializer


class LossViewSet(viewsets.ModelViewSet):  # new
    queryset = Loss.objects.all()
    serializer_class = LossSerializer
