from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from zeusapi.helpers import PathAndRename


class Aimodel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)
    version = models.CharField(blank=True, max_length=255, default='0.0.1')
    purpose = models.TextField(blank=True)

    active = models.BooleanField(default=True)

    AIMODEL_TYPE = [

        ('NA', 'Not Available'),   
    ]

    aimodel_type = models.CharField(
        max_length=2,
        choices=AIMODEL_TYPE,
        default='NA',
    )          

    def __str__(self):
        return self.name
