from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @list_route(['GET'], permission_classes=[AllowAny])
    def is_logged(self, request):
        """
        Response body: \n
        `is_logged` (boolean)
        """

        result = {
            "is_logged": not request.user.is_anonymous
        }

        return Response(result)

    @list_route(['GET'], permission_classes=[IsAuthenticated])
    def details(self, request):
        """
        Response body: \n
        `first_name` (string) \n
        `last_name` (string)

        If user is not logged in, this view returns HTTP 403.
        """

        user = request.user

        result = {
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

        return Response(result)
