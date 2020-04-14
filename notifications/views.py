
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
    Notification, 
)

from .serializers import (
    NotificationSerializer, 
)


class NotificationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
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
            queryset = Notification.objects.all()
        elif user.user_type == 'LV':
            pass
        elif user.user_type == 'HT':
            pass
        elif user.user_type == 'UT':
            pass                
        else:
            queryset = Notification.objects.none()

        return queryset  
          


    @action(methods=['GET'], detail=False)
    def read(self, request, *args, **kwargs):
        read_notification = Notification.objects.all().filter(read=True)

        page = self.paginate_queryset(read_notification)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(read_notification, many=True)
        return Response(serializer.data)          

    @action(methods=['GET'], detail=False)
    def unread(self, request, *args, **kwargs):
        unread_notification = Notification.objects.all().filter(read=False)

        page = self.paginate_queryset(unread_notification)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(unread_notification, many=True)
        return Response(serializer.data)      

    @action(methods=['GET'], detail=True)
    def mark_read(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.read = True

        serializer =  NotificationSerializer(notification)
        return Response(serializer.data)   

    @action(methods=['GET'], detail=True)
    def mark_unread(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.read = False

        serializer =  NotificationSerializer(notification)
        return Response(serializer.data)      

    @action(methods=['GET'], detail=False)
    def sent(self, request, *args, **kwargs):
        sent_notification = Notification.objects.all().filter(sent=True)

        page = self.paginate_queryset(sent_notification)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(sent_notification, many=True)
        return Response(serializer.data)          

    @action(methods=['GET'], detail=False)
    def unsent(self, request, *args, **kwargs):
        unsent_notification = Notification.objects.all().filter(sent=False)

        page = self.paginate_queryset(unsent_notification)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(unsent_notification, many=True)
        return Response(serializer.data)        