from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        """
        Create test instances of the Menu model.
        """
        self.client = APIClient()  # Use DRF's test client for API testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        self.menu1 = MenuItem.objects.create(title="Pizza", price=12.50, inventory=10)
        self.menu2 = MenuItem.objects.create(title="Burger", price=8.50, inventory=20)

    def test_getall(self):
        """
        Test retrieving all Menu objects and asserting serialized data.
        """
        response = self.client.get(reverse('menu-items'))  # Call the API endpoint
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        # Check response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
