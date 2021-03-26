from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class BasketballPlayer(Athlete):
    points_scored = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    rebounds = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class SoccerPlayer(Athlete):
    goals_scored = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    yellow_cards = models.PositiveIntegerField()

    def __str__(self):
        return self.name
