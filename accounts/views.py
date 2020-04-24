
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
    Account, 
)

from .serializers import (
    AccountSerializer, 
)


class AccountViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
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
            queryset = Account.objects.all()

        elif user.user_type == 'LV':
            queryset = Account.objects.all()

        elif user.user_type == 'HT':
            queryset = Account.objects.all()

        elif user.user_type == 'UT':
            queryset = Account.objects.all()

        else:
            queryset = Account.objects.none()

        return queryset  
          

    @action(methods=['GET'], detail=True)
    def activate(self, request, *args, **kwargs):
        account = self.get_object()
        account.active = True

        serializer =  AccountSerializer(account)
        return Response(serializer.data)   

    @action(methods=['GET'], detail=True)
    def deactivate(self, request, *args, **kwargs):
        account = self.get_object()
        account.active = False

        serializer =  AccountSerializer(account)
        return Response(serializer.data)                    


"""
    @action(methods=['GET'], detail=False)
    def lol(self, request, *args, **kwargs):

        from django.core.files.storage import default_storage
        file = default_storage.open('storage_test', 'w')
        file.write('storage contents')
        file.close()
        print(default_storage.exists('storage_test'))
        file = default_storage.open('storage_test', 'r')
        print(file.read())
        file.close()

        return 'lol'
        #target_user = int(kwargs['target_id'])
        #Follow.objects.create(user=user, target=target_user)
        #return Response(status=status.HTTP_204_NO_CONTENT)            
"""