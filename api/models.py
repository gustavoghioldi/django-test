import uuid
from django.db import models
from django.utils import timezone
# Create your models here.

class TicketModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    artist = models.CharField(max_length=128)
    date = models.DateTimeField(default=timezone.now())
    