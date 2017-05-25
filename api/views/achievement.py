from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from api.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    