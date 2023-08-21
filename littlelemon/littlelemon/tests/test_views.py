from django.test import TestCase
from restaurant.models import MenuItem
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Cake", price=150, inventory=50)

    def test_getall(self):
        client = APIClient()
        response = client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
