
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
    Gateway, 
)

from .serializers import (
    GatewaySerializer, 
)


class GatewayViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        permission_classes = [AllowAny]#[IsAuthenticated]
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        """
        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        user = self.request.user
        queryset = Gateway.objects.all()
        """
        if user.user_type == 'SU':
            queryset = Gateway.objects.all()
        elif user.user_type == 'LV':
            queryset = Gateway.objects.all()
        elif user.user_type == 'HT':
            queryset = Gateway.objects.all()
        elif user.user_type == 'UT':
            queryset = Gateway.objects.all()                
        else:
            queryset = Gateway.objects.none()  
        """      
        return queryset  
          


    @action(methods=['GET'], detail=True)
    def activate(self, request, *args, **kwargs):
        plant = self.get_object()
        plant.active = True

        serializer =  GatewaySerializer(plant)
        return Response(serializer.data)   

    @action(methods=['GET'], detail=True)
    def deactivate(self, request, *args, **kwargs):
        plant = self.get_object()
        plant.active = False

        serializer =  GatewaySerializer(plant)
        return Response(serializer.data)             