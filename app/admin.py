from django.contrib import admin
from app.models import Team, Game, Win, Loss

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'coach', 'category',
                    'games_played', 'points', 'wins', 'losses')

    def games_played(self, obj):
        return obj.calculate_games_played()

    def points(self, obj):
        return obj.calculate_points()

    def wins(self, obj):
        return obj.calculate_wins()

    def losses(self, obj):
        return obj.calculate_losses()


admin.site.register(Team, TeamAdmin)
admin.site.register(Game)
# admin.site.register(Win)
# admin.site.register(Loss)
