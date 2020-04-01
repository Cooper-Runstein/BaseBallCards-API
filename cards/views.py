from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from cards.serializers import UserSerializer, GroupSerializer, BaseBallCardSerializer
from cards.models import BaseBallCard


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BaseBallCardViewSet(viewsets.ModelViewSet):
    queryset = BaseBallCard.objects.all()
    serializer_class = BaseBallCardSerializer
    permissions_classes = [permissions.IsAuthenticated]
