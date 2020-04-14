from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from zeusapi.helpers import PathAndRename

from users.models import CustomUser


class Notification(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.CharField(blank=False, max_length=255)

    created = models.BooleanField(default=True)
    sent = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.message
