# Generated by Django 4.2 on 2023-04-15 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("men", "0002_team_games_played"),
    ]

    operations = [
        migrations.DeleteModel(
            name="GamePlayed",
        ),
    ]
