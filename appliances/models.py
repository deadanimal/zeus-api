from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from zeusapi.helpers import PathAndRename

from accounts.models import (Account)
from buildings.models import (Building)

class ApplianceBase(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    active = models.BooleanField(default=True)
    
    brand = models.CharField(null=True, max_length=255)
    model = models.CharField(null=True, max_length=255)
    year = models.CharField(null=True, max_length=255)
    manufacturer = models.CharField(null=True, max_length=255)

    def __str__(self):
        name_string = self.brand + '-' + self.model + '-' + self.year
        return name_string

class Appliance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    active = models.BooleanField(default=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)

    appliance_base = models.ForeignKey(ApplianceBase, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name    

class ApplianceTransaction(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_datetime = models.DateTimeField(null=True)
    
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, null=True)

    STATUS = [
        ('NA', 'Not Available'),   
    ] 

    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default='NA',
    )    