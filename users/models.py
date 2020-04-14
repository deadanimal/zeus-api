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

    active = models.BooleanField(default=False)
    enabled = models.BooleanField(default=False)

    billing_address = models.CharField(blank=True, max_length=255)

    USER_TYPE = [
        ('LV', 'Low Voltage'), 
        ('HT', 'High Tension'), 
        ('UT', 'Utility'), 
        ('PP', 'Power Producer'), 
        ('SU', 'Superuser'), 


        ('NA', 'Not Available'),   
    ]

    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE,
        default='NA',
    )        
   
    
    def __str__(self):
        return self.name



class UserSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name            


class UserLowVoltage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name       

class UserHighTension(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name           