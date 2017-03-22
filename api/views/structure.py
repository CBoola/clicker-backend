from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from api.models import Structure


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = '__all__'


class StructureViewSet(viewsets.ModelViewSet):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
