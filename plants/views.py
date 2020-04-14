
from django.shortcuts import render
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Plant, 
)

from .serializers import (
    PlantSerializer, 
)


class PlantViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Plant.objects.all()
        return queryset  
          


    @action(methods=['GET'], detail=True)
    def activate(self, request, *args, **kwargs):
        plant = self.get_object()
        plant.active = True

        serializer =  PlantSerializer(plant)
        return Response(serializer.data)   

    @action(methods=['GET'], detail=True)
    def deactivate(self, request, *args, **kwargs):
        plant = self.get_object()
        plant.active = False

        serializer =  PlantSerializer(plant)
        return Response(serializer.data)             