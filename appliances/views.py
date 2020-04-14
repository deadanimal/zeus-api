
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
    Appliance, 
    ApplianceBase,
    ApplianceTransaction
)

from .serializers import (
    ApplianceSerializer, 
    ApplianceBaseSerializer,
    ApplianceTransactionSerializer
)


class ApplianceViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Appliance.objects.all()
        return queryset  
          


    @action(methods=['GET'], detail=True)
    def activate(self, request, *args, **kwargs):
        appliance = self.get_object()
        appliance.active = True

        serializer =  ApplianceSerializer(appliance)
        return Response(serializer.data)   

    @action(methods=['GET'], detail=True)
    def deactivate(self, request, *args, **kwargs):
        appliance = self.get_object()
        appliance.active = False

        serializer =  ApplianceSerializer(appliance)
        return Response(serializer.data)    


class ApplianceBaseViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ApplianceBase.objects.all()
    serializer_class = ApplianceBaseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = ApplianceBase.objects.all()
        return queryset  

    @action(methods=['GET'], detail=True)
    def activate(self, request, *args, **kwargs):
        appliance = self.get_object()
        appliance.active = True

        serializer =  ApplianceBaseSerializer(appliance)
        return Response(serializer.data)   

    @action(methods=['GET'], detail=True)
    def deactivate(self, request, *args, **kwargs):
        appliance = self.get_object()
        appliance.active = False

        serializer =  ApplianceBaseSerializer(appliance)
        return Response(serializer.data)            



class ApplianceTransactionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ApplianceTransaction.objects.all()
    serializer_class = ApplianceTransactionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = ApplianceTransaction.objects.all()
        return queryset          


    @action(methods=['GET'], detail=False)
    def latest(self, request, *args, **kwargs):
        appliance = self.get_object()

        serializer =  ApplianceSerializer(appliance)
        return Response(serializer.data)         