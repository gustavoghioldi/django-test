from rest_framework.serializers import ModelSerializer
from .models import TicketModel

class TicketSerializer(ModelSerializer):
    class Meta:
        model = TicketModel
        fields = "__all__"