from django.urls import path

from .views import PetViewSet, ShelterViewSet, AdoptPetView

urlpatterns = [
    path('pets', PetViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('pets/<int:pk>', PetViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('pets/<int:pk>/adopt/', AdoptPetView.as_view()),
    path('shelter', ShelterViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('shelter/<int:pk>', ShelterViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
