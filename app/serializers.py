from app.models import Team, Game, Win, Loss

from rest_framework import serializers


class WinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Win
        fields = '__all__'


class LossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loss
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    wins = WinSerializer()
    losses = LossSerializer()

    class Meta:
        model = Team
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()

    class Meta:
        model = Game
        fields = '__all__'
