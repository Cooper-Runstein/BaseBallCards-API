from django.db import models
from enum import Enum


class TeamOption(models.TextChoices):
    ARI = "Arizona Diamondbacks"
    ATL = "Atlanta Braves"
    BLT = "Baltimore Orioles"
    BOS = "Boston Red Sox"
    CWS = "Chicago White Sox"
    CHI = "Chicago Cubs"
    CIN = "Cincinnati Reds"
    CLE = "Cleveland Indians"
    COL = "Colorado Rockies"
    DET = "Detroit Tigers"
    HOU = "Houston Astros"
    KCR = "Kansas City Royals"
    LAA = "Los Angeles Angels"
    LAD = "Los Angeles Dodgers"
    MIA = "Miami Marlins"
    MIL = "Milwaukee Brewers"
    MIN = "Minnesota Twins"
    NYY = "New York Yankees"
    NYM = "New York Mets"
    OAK = "Oakland Athletics"
    PHI = "Philadelphia Phillies"
    PIT = "Pittsburgh Pirates"
    SDP = "San Diego Padres"
    SFG = "San Francisco Giants"
    SEA = "Seattle Mariners"
    STL = "St. Louis Cardinals"
    TBR = "Tampa Bay Rays"
    TEX = "Texas Rangers"
    TOR = "Toronto Blue Jays"
    WSH = "Washington Nationals"


class BaseModel(models.Model):
    class Meta:
        app_label = 'cards'
        abstract = True


class Company(BaseModel):
    name = models.CharField(max_length=30)


class Player(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(blank=True)


class Team(BaseModel):
    team = models.CharField(
        max_length=30,
        choices=TeamOption.choices,
    )


class BaseBallCard(BaseModel):
    year = models.IntegerField()

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
