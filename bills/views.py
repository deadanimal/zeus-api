
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
    Bill, 
)

from .serializers import (
    BillSerializer, 
)


class BillViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        permission_classes = [AllowAny] #[IsAuthenticated]

        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        """
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        queryset = Bill.objects.all()

        """
        if user.user_type == 'SU':
            queryset = Bill.objects.all()
        elif user.user_type == 'LV':
            queryset = Bill.objects.all()
        elif user.user_type == 'HT':
            queryset = Bill.objects.all()
        elif user.user_type == 'UT':
            queryset = Bill.objects.all()                
        else:
            queryset = Bill.objects.none()        
        """
        return queryset  
          


    @action(methods=['GET'], detail=False)
    def paid(self, request, *args, **kwargs):
        paid_bill = Bill.objects.all().filter(bill_paid=True)

        page = self.paginate_queryset(paid_bill)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(paid_bill, many=True)
        return Response(serializer.data)          

    @action(methods=['GET'], detail=False)
    def unpaid(self, request, *args, **kwargs):
        unpaid_bill = Bill.objects.all().filter(bill_paid=False)

        page = self.paginate_queryset(unpaid_bill)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(unpaid_bill, many=True)
        return Response(serializer.data)           