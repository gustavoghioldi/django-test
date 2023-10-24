from django.contrib import admin
from .models import TicketModel

@admin.register(TicketModel)
class TicketAdmin(admin.ModelAdmin):
    pass