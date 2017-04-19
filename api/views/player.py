from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from api.models import Player, Structure, Upgrade
from api.validators import validate_schema, validate_existence
from api.schemas import *


class PlayerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, player):
        return player.user == request.user or request.user.is_staff


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["pk", "name", "current_state", "structures", "upgrades", "statistics"]
        read_only_fields = ["name"]

    name = serializers.SerializerMethodField()
    current_state = serializers.JSONField(
        validators=[
            validate_schema(CURRENT_STATE_SCHEMA)
        ])

    structures = serializers.JSONField(
        validators=[
            validate_schema(STRUCTURES_SCHEMA),
            validate_existence(Structure.objects.all())
        ])
    upgrades = serializers.JSONField(
        validators=[
            validate_schema(UPGRADES_SCHEMA),
            validate_existence(Upgrade.objects.all())
        ])

    statistics = serializers.JSONField(
        validators=[
            validate_schema(STATISTICS_SCHEMA)
        ])

    def get_name(self, player):
        return player.__str__()


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    #permission_classes = [PlayerPermission]

    def list(self, request):
        if not IsAdminUser().has_permission(request, self):
            raise PermissionDenied()

        result = PlayerSerializer(self.queryset, many=True)
        return Response(result.data)

    def rec(self, request):
        if not IsAdminUser().has_permission(request, self):
            raise PermissionDenied()

        result = PlayerSerializer(self.queryset, many=True)
        return Response(result.data)

    #@list_route(['GET'], permission_classes=[AllowAny])
    @list_route(['GET'])
    def is_logged(self, request):
        """
        This endpoint is used to check if the user is logged in and can be treated
        as a player. If user is logged in, additional information is provided.

        Response body: \n
        `is_logged` (boolean) \n
        `player_id` (integer) - this ID should be used to consume the user API \n
        `is_new` (boolean) - true if the player model is newly created.
            Can be used to implement a "welcome message"
        """

        # administrator is not the user!
        is_logged = Player.is_user_logged(request.user)

        result = {
            "is_logged": is_logged,
        }

        if is_logged:
            player, is_new = Player.objects.get_or_create(user=request.user)

            result["player_id"] = player.pk
            result["is_new"] = is_new

        return Response(result)
