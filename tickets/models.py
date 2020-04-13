from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from zeusapi.helpers import PathAndRename

from users.models import CustomUser

class Ticket(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    active = models.BooleanField(default=True)

    TICKET_TYPE = [

        ('AR', 'Architect'),  
        ('AN', 'Analyst'),  
        ('DV', 'Developer'),  

        ('NA', 'Not Available'),   
    ] 

    ticket_type = models.CharField(
        max_length=2,
        choices=TICKET_TYPE,
        default='NA',
    )    

    def __str__(self):
        return self.name


class TicketMessage(models.Model):        

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField(default='NA')

    sent = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    sent_datetime = models.DateTimeField(null=True)
    received_datetime = models.DateTimeField(null=True)
    read_datetime = models.DateTimeField(null=True)

    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ticket_message_sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ticket_message_receiver')