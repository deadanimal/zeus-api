import json
import time

from django.http import JsonResponse
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
    Device, 
)

from .serializers import (
    DeviceSerializer, 
)

from .helpers import (
    device_reading
)


class DeviceViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        """
        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        user = self.request.user

        if user.user_type == 'SU':
            queryset = Device.objects.all()
        elif user.user_type == 'LV':
            queryset = Device.objects.all()
        elif user.user_type == 'HT':
            queryset = Device.objects.all()
        elif user.user_type == 'UT':
            queryset = Device.objects.all()                
        else:
            queryset = Device.objects.none()
        return queryset  


    @action(methods=['GET'], detail=True)
    def reading(self, request, *args, **kwargs):
        device = self.get_object()

        frequency = request.GET.get('frequency', '') # minute, hour, day
        end_date = request.GET.get('end', '') # time in seconds since epoch(Unix)

        if frequency and end_date:

            if int(end_date) > int(time.time()):
                end_date = int(time.time())

            message = device_reading(
                device.id,
                frequency, 
                end_date)
        else:
            default_end_date = int(time.time())
            default_start_date = default_end_date - 86400
            message = device_reading(
                device.id,
                'second', 
                default_end_date)
        
        return JsonResponse(message)


    @action(methods=['GET'], detail=False)
    def lol(self, request, *args, **kwargs):
        """
        from django.core.files.storage import default_storage
        file = default_storage.open('storage_test', 'w')
        file.write('storage contents')
        file.close()
        print(default_storage.exists('storage_test'))
        file = default_storage.open('storage_test', 'r')
        print(file.read())
        file.close()
        """

        return 'lol'
        #target_user = int(kwargs['target_id'])
        #Follow.objects.create(user=user, target=target_user)
        #return Response(status=status.HTTP_204_NO_CONTENT)        
        #     