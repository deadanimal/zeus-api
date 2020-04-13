# users/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)

    """
    USER_TYPE = [

        ('NA', 'Not Available'),   
    ]

    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE,
        default='NA',
    )        

    EMPLOYEE_TYPE = [

        ('AR', 'Architect'),  
        ('AN', 'Analyst'),  
        ('DV', 'Developer'),  

        ('NA', 'Not Available'),   
    ] 

    employee_type = models.CharField(
        max_length=2,
        choices=EMPLOYEE_TYPE,
        default='NA',
    )    
    """
    def __str__(self):
        return self.name