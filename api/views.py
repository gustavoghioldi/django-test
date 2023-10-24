
from rest_framework import generics
from rest_framework.views import APIView, Response
from rest_framework.exceptions import APIException
from .serializers import TicketSerializer
from .models import TicketModel
from .services import count_tickets, last_ticket

class TicketView(generics.ListCreateAPIView):
    queryset = TicketModel.objects.all()
    serializer_class = TicketSerializer

class QueryView(APIView):
    def get(self, request):
        if request.GET.get("query") == "count":
            total = count_tickets()
            return Response({"total":total})
        if request.GET.get("query") == "last":
            last = last_ticket()
            return Response(last)
        else:
            raise APIException({"detail":"no se encontro query"}, 400)
