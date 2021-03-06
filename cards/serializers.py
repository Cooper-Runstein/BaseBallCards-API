from django.contrib.auth.models import User, Group
from rest_framework import serializers

from cards.models import BaseBallCard, Player


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BaseBallCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseBallCard
        fields = ['year', "player", "team", "company"]
        depth = 1


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["first_name", "last_name"]
