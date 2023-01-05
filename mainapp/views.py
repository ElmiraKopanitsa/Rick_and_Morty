from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Location, Character, Epizod
from .serializers import LocationSerializer, CharacterSerializer, EpizodSerializer, CreateEpizodSerializer


class LocationModelViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CharacterModelViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class EpizodeModelViewSet(ModelViewSet):
    queryset = Epizod.objects.all()
    serializer_class = CreateEpizodSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = EpizodSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EpizodSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EpizodSerializer(instance)
        return Response(serializer.data)

