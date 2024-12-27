# from django.test import TestCase
# from django.urls import reverse
# from restaurant.models import MenuItem
# from rest_framework import status
# from rest_framework.test import APIClient

# class MenuViewTest(TestCase):
    
#     def setUp(self):
#         MenuItem.objects.create(title="IceCream", price=80)
#         MenuItem.objects.create(title="Burger", price=120)
        
#     def test_getall(self):
#         # Set up API client
#         client = APIClient()
        
#         # Make a GET request to the API endpoint
#         response = client.get(reverse('menu-list'))  # Assuming 'menu-list' is the URL for the list view
        
#         # Assert that the response status is OK
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#         # Assert that the response contains the serialized data
#         expected_data = [
#             {"title": "IceCream", "price": "80.00"},
#             {"title": "Burger", "price": "120.00"}
#         ]
        
#         self.assertEqual(response.json(), expected_data)

from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuItem
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    
    def setUp(self):
        """
        This method runs before each test. We create two menu items to be used in the tests.
        """
        self.menu_item1 = MenuItem.objects.create(title="IceCream", price=80)
        self.menu_item2 = MenuItem.objects.create(title="Burger", price=120)
        
        self.client = APIClient()  # Instantiate API client for making requests
        
    def test_get_all_menu_items(self):
        """
        Test the GET request to retrieve all MenuItem objects and check if the 
        response status is OK and the returned data matches the expected format.
        """
        response = self.client.get(reverse('menuitem-list'))  # 'menuitem-list' should be the name of your URL for ListCreateAPIView
        
        # Assert that the response status is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response contains the serialized data for the two menu items
        expected_data = [
            {"title": "IceCream", "price": "80.00"},
            {"title": "Burger", "price": "120.00"}
        ]
        
        # Check if the response data matches the expected data
        self.assertEqual(response.json(), expected_data)

    def test_create_menu_item(self):
        """
        Test the POST request to create a new MenuItem object and check if the 
        response status is created (201) and the new item is returned correctly.
        """
        new_item_data = {
            "title": "Pizza",
            "price": 150.0
        }

        response = self.client.post(reverse('menuitem-list'), new_item_data, format='json')
        
        # Assert that the response status is HTTP 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert that the newly created item matches the data sent
        self.assertEqual(response.data['title'], new_item_data['title'])
        self.assertEqual(float(response.data['price']), new_item_data['price'])

    def test_get_single_menu_item(self):
        """
        Test the GET request to retrieve a single MenuItem object by its ID.
        """
        response = self.client.get(reverse('menuitem-detail', args=[self.menu_item1.id]))  # 'menuitem-detail' should be the name of your URL for RetrieveUpdateAPIView
        
        # Assert that the response status is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response data matches the menu item
        self.assertEqual(response.data['title'], self.menu_item1.title)
        self.assertEqual(float(response.data['price']), self.menu_item1.price)

    def test_update_menu_item(self):
        """
        Test the PUT request to update a MenuItem object and check if the 
        response reflects the updated data.
        """
        updated_data = {
            "title": "Chocolate Cake",
            "price": 110.0
        }

        response = self.client.put(reverse('menuitem-detail', args=[self.menu_item1.id]), updated_data, format='json')
        
        # Assert that the response status is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that the updated data is correct
        self.assertEqual(response.data['title'], updated_data['title'])
        self.assertEqual(float(response.data['price']), updated_data['price'])

    def test_delete_menu_item(self):
        """
        Test the DELETE request to remove a MenuItem object and check if the 
        response status is HTTP 204 NO CONTENT.
        """
        response = self.client.delete(reverse('menuitem-detail', args=[self.menu_item2.id]))
        
        # Assert that the response status is HTTP 204 NO CONTENT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Assert that the item is actually deleted (it should not exist in the database anymore)
        self.assertFalse(MenuItem.objects.filter(id=self.menu_item2.id).exists())
