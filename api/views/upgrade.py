from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from api.models import Upgrade


class UpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upgrade
        fields = '__all__'


class UpgradeViewSet(viewsets.ModelViewSet):
    queryset = Upgrade.objects.all()
    serializer_class = UpgradeSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
