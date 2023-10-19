from rest_framework import serializers

from .models import Pet, Shelter


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.tutor = self.context['request'].user.tutor
        instance.adopted = True
        instance.save()
        return instance


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'
