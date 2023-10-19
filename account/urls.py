from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path('accounts', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('accounts/<int:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
