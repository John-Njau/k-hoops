# Generated by Django 4.2 on 2023-04-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_game_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="venue",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]