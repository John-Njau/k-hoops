# Generated by Django 4.2 on 2023-04-16 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("team1_score", models.IntegerField()),
                ("team2_score", models.IntegerField()),
                ("date", models.DateField()),
                ("time", models.TimeField(blank=True, null=True)),
                ("venue", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("coach", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[("M", "Men"), ("W", "Women")], max_length=1
                    ),
                ),
                (
                    "division",
                    models.CharField(
                        choices=[("KBF", "KBF"), ("DIV1", "DIV1"), ("DIV2", "DIV2")],
                        max_length=4,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Win",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField(default=0)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.game"
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.team"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Loss",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField(default=0)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.game"
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.team"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="game",
            name="team1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team1",
                to="app.team",
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="team2",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team2",
                to="app.team",
            ),
        ),
    ]
