from django.test import TestCase
from rest_framework.test import APIRequestFactory
import json
from .models import TicketModel
from .services import last_ticket, count_tickets
from .views import TicketView

def create_dataset():
    TicketModel.objects.create(
            artist="Sodom",
            date="2023-10-30T00:00:00Z"
        )
    
class ApiTestCase(TestCase):
    def setUp(self) -> None:
        create_dataset()

    def test_create_ticket(self):
        data = {
          "artist": "Metallica",
          "date": "2023-11-30T21:00:00Z"
        }
        factory = APIRequestFactory()
        request = factory.post('/tickets', data=data)
        view = TicketView.as_view()
        response = view(request)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(TicketModel.objects.count(), 2)

    def test_create_without_artist(self):
        data = {
          "date": "2023-11-30T21:00:00Z"
        }
        factory = APIRequestFactory()
        request = factory.post('/tickets', data=data)
        view = TicketView.as_view()
        response = view(request)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(TicketModel.objects.count(), 1)

    def test_create_without_date(self):
        data = {
          "artist": "Metallica",
        }
        factory = APIRequestFactory()
        request = factory.post('/tickets', data=data)
        view = TicketView.as_view()
        response = view(request)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(TicketModel.objects.count(), 1)

    def test_create_with_blank_body(self):
        data = None
        factory = APIRequestFactory()
        request = factory.post('/tickets', data=data)
        view = TicketView.as_view()
        response = view(request)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(TicketModel.objects.count(), 1)

    def test_list_tickets(self):
        factory = APIRequestFactory()
        request = factory.get('/tickets')
        view = TicketView.as_view()
        response = view(request)

        response_data = json.loads(response.render().content)
        self.assertEquals(response_data[0]["artist"], "Sodom")
        self.assertEquals(response_data[0]["date"], "2023-10-30T00:00:00Z")
        self.assertTrue(type(response_data[0]["uuid"]) is str)

class QueryViewTestCase(TestCase):
    def setUp(self) -> None:
        create_dataset()
    def test_count(self):
        pass

    def test_last(self):
        pass

    def test_without_query(self):
        pass

    def test_with_wrong_query(self):
        pass

class ServicesTestCase(TestCase):
    def setUp(self) -> None:
        TicketModel.objects.create(
            artist="Sodom",
            date="2023-10-30T00:00:00Z"
        )


    def test_last_ticket_artist(self):
        self.assertEquals(str(last_ticket()["artist"]), "Sodom")

    def test_count_tickets(self):
        self.assertEquals(count_tickets(), 1)