from rest_framework import serializers
from .models import Location, Character, Epizod


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'world', 'description', 'image']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'birth_location', 'location', 'description', 'image', 'gender', 'race', 'alive']


class EpizodSerializer(serializers.ModelSerializer):
    characters = serializers.StringRelatedField(many=True)
    class Meta:
        model = Epizod
        fields = ['id', 'name', 'number', 'number_season', 'image', 'description', 'premiere', 'characters']


class CreateEpizodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epizod
        fields = ['id', 'name', 'number', 'number_season', 'image', 'description', 'premiere', 'characters']
