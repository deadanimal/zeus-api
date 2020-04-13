from __future__ import unicode_literals 

import uuid 
from datetime import datetime    

import django
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from zeusapi.helpers import PathAndRename

from organisations.models import Organisation
from users.models import CustomUser

class Account(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)
    account_number = models.CharField(blank=True, max_length=255)

    active = models.BooleanField(default=True)

    account_created = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    linked_organisation = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name='account_linked_organisation')
    linked_user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name='account_linked_user')

    def __str__(self):
        return self.name
