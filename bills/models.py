from __future__ import unicode_literals 

import uuid 
from datetime import datetime

import django
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from zeusapi.helpers import PathAndRename


class Bill(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    status = models.CharField(blank=False, max_length=255, default='NA')

    date_generated = models.DateTimeField(default=django.utils.timezone.now)
    date_invoiced = models.DateTimeField(default=django.utils.timezone.now)
    date_due_date = models.DateTimeField(default=django.utils.timezone.now)
    date_paid = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name
