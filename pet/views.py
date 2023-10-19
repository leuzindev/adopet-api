from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Pet, Shelter
from .serializers import PetSerializer, ShelterSerializer


class PetViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'adopted']
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer


class AdoptPetView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        return {'request': self.request}

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if hasattr(request.user, 'organization'):
            instance.adopted = False
            instance.tutor = None
        else:
            instance.adopted = True
            instance.tutor = request.user.tutor

        instance.save()
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
