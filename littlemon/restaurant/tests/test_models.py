from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice Cream", price=80, inventory=100)
        # self.assertEqual(item.get_item(), "Ice Cream : 80")
        self.assertEqual(str(item), "IceCream : 80")