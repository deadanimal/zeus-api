
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
    Organisation, 
)

from .serializers import (
    OrganisationSerializer, 
)


class OrganisationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
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
            queryset = Organisation.objects.all()
        elif user.user_type == 'LV':
            pass
        elif user.user_type == 'HT':
            pass
        elif user.user_type == 'UT':
            pass                
        else:
            queryset = Organisation.objects.none()        
        return queryset  
          

    @action(methods=['GET'], detail=True)
    def activate(self, request, *args, **kwargs):
        organisation = self.get_object()
        organisation.active = True

        serializer =  OrganisationSerializer(organisation)
        return Response(serializer.data)   

    @action(methods=['GET'], detail=True)
    def deactivate(self, request, *args, **kwargs):
        organisation = self.get_object()
        organisation.active = False

        serializer =  OrganisationSerializer(organisation)
        return Response(serializer.data)        


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