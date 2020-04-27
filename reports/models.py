from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from zeusapi.helpers import PathAndRename


class Report(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=255)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
