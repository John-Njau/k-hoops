from django.contrib import admin

from app.models import Team, Game


# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'coach', 'category',
                    'games_played', 'wins', 'losses','points')

    list_filter = ('category', 'division')

    def games_played(self, obj):
        return obj.calculate_games_played()

    def points(self, obj):
        return obj.calculate_points()

    def wins(self, obj):
        return obj.calculate_wins()

    def losses(self, obj):
        return obj.calculate_losses()


class GameAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'score', 'date', 'venue', 'time', 'latest_game')

    def score(self, obj):
        return f"{obj.team1_score} - {obj.team2_score}"
    
    def latest_game(self, obj):
        return obj.get_latest_game()


admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
# admin.site.register(Win)
# admin.site.register(Loss)
