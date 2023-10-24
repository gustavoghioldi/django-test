from .models import TicketModel
from django.forms import model_to_dict
def count_tickets():
    return TicketModel.objects.count()


def last_ticket():
    return model_to_dict(TicketModel.objects.last())