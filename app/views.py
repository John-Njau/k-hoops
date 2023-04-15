from django.shortcuts import render
from app.models import Team, Game, Win, Loss
from app.serializers import TeamSerializer, GameSerializer, WinSerializer, LossSerializer
from rest_framework import viewsets
from django.views import View
from django.http import HttpResponse
from django.template import loader

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


class GamesView(View):
    template_name = 'gamesStats.html'

    def get(self, request, *args, **kwargs):
        teams = Team.objects.all()
        team_data = []
        index_counter = 1


        for team in teams:
            data = {
                'index': index_counter,
                'name': team.name,
                'coach': team.coach,
                'category': team.category,
                'games_played': team.calculate_games_played(),
                'points': team.calculate_points(),
                'wins': team.calculate_wins(),
                'losses': team.calculate_losses(),
            }
            team_data.append(data)

            # Increment the index counter
            index_counter += 1

        # Sort team_data by points in descending order
        team_data = sorted(team_data, key=lambda x: int(x['points']), reverse=True)

        context = {
            'title': 'Team Stats',
            'team_data': team_data,
        }

        return render(request, self.template_name, context)


class LatestGame(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        games = Game.objects.all()
        game_data = []

        latest_game = Game.objects.latest('date')
        latest_game_data = {
            'team1': latest_game.team1,
            'team2': latest_game.team2,
            'team1_score': latest_game.team1_score,
            'team2_score': latest_game.team2_score,
            'date': latest_game.date,
            'time': latest_game.time,
            'venue': latest_game.venue,
        }

        for game in games:
            data = {
                'team1': game.team1,
                'team2': game.team2,
                'team1_score': game.team1_score,
                'team2_score': game.team2_score,
                'date': game.date,
                'time': game.time,
                'venue': game.venue,
            }
            game_data.append(data)

        context = {
            'title': 'Latest Game',
            'game_data': game_data,
            'latest_game': latest_game_data,
        }

        return render(request, self.template_name, context)
