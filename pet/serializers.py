from rest_framework import serializers

from .models import Pet, Shelter


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
