from django.db import models
from django.utils import timezone


class Team(models.Model):
    MEN = "M"
    WOMEN = "W"
    TEAM_CATEGORY_CHOICES = [
        (MEN, "Men"),
        (WOMEN, "Women"),
    ]

    KBF = "KBF"
    DIV1 = "DIV1"
    DIV2 = "DIV2"

    TEAM_DIVISION_CHOICES = [
        (KBF, "KBF"),
        (DIV1, "DIV1"),
        (DIV2, "DIV2"),
    ]

    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=TEAM_CATEGORY_CHOICES)
    division = models.CharField(max_length=4, choices=TEAM_DIVISION_CHOICES)

    def calculate_games_played(self):
        games = Game.objects.filter(
            team1=self) | Game.objects.filter(team2=self)
        return len(games)

    def calculate_points(self):
        wins = Win.objects.filter(team=self)
        losses = Loss.objects.filter(team=self)
        points = 0
        for win in wins:
            points += win.count * 2
        for loss in losses:
            points += loss.count
        return points

    def calculate_wins(self):
        wins = Win.objects.filter(team=self)
        count = 0
        for win in wins:
            count += win.count
        return count

    def calculate_losses(self):
        losses = Loss.objects.filter(team=self)
        count = 0
        for loss in losses:
            count += loss.count
        return count

    def __str__(self):
        return self.name


class Game(models.Model):
    team1 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team2')
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    venue = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.team1} vs {self.team2}'

    @classmethod
    def get_latest_game(cls):
        now = timezone.now()
        return cls.objects.filter(date__lte=now.date(), time__lte=now.time()).latest('date', 'time')

    def save(self, *args, **kwargs):
        super(Game, self).save(*args, **kwargs)

        if self.team1_score > self.team2_score:
            try:
                win = Win.objects.get(team=self.team1, game=self)
                win.count += 1
                win.save()
            except Win.DoesNotExist:
                win = Win.objects.create(team=self.team1, count=1, game=self)
                win.save()

            try:
                loss = Loss.objects.get(team=self.team2, game=self)
                loss.count += 1
                loss.save()
            except Loss.DoesNotExist:
                loss = Loss.objects.create(team=self.team2, count=1, game=self)
                loss.save()
        elif self.team1_score < self.team2_score:
            try:
                win = Win.objects.get(team=self.team2, game=self)
                win.count += 1
                win.save()
            except Win.DoesNotExist:
                win = Win.objects.create(team=self.team2, count=1, game=self)
                win.save()

            try:
                loss = Loss.objects.get(team=self.team1, game=self)
                loss.count += 1
                loss.save()
            except Loss.DoesNotExist:
                loss = Loss.objects.create(team=self.team1, count=1, game=self)
                loss.save()

        super(Game, self).save(*args, **kwargs)


class Win(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.team.name} won {self.count} games'


class Loss(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.team.name} lost {self.count} games'
