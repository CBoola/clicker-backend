from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from api.models.player import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAdminUser]


    @list_route(['GET'], permission_classes=[AllowAny])
    def is_logged(self, request):
        """
        Response body: \n
        `is_logged` (boolean)
        """

        # administrator is not the user!
        is_logged = request.user.is_authenticated() and not request.user.is_staff

        result = {
            "is_logged": is_logged,
        }

        if is_logged:
            player, is_new = Player.objects.get_or_create(user=request.user)

            result["player_id"] = player.pk
            result["is_new"] = is_new

        return Response(result)
