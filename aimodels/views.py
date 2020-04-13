

from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from django.core.files.storage import default_storage

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Aimodel, 
)

from .serializers import (
    AimodelSerializer, 
)



appliance_detection_model = default_storage.open('aimodels/appliance_detection.pkl', 'r')



class AimodelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Aimodel.objects.all()
    serializer_class = AimodelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Aimodel.objects.all()
        return queryset  


    @action(methods=['POST'], detail=False)
    def predict(self, request, *args, **kwargs):    

        file_sent = request.data
        params = request.query_params

        if params['model'] == 'appliance':
            print('appliance')
        
        message = {'app': 123}
        
        return JsonResponse(message)              


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