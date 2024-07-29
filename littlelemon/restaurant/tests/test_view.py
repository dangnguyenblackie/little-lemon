from django.test import TestCase
from restaurant.models import MenuItem

class MenuViewTest (TestCase):

    def setUp(self):
        MenuItem.objects.create(title='Pizza', price=150, inventory=30)
        MenuItem.objects.create(title='Hamburger', price=100, inventory=70)
        MenuItem.objects.create(title='LemonCake', price=90, inventory=100)

    def test_getall(self):
        queryset = MenuItem.objects.all()
        returnedRes = [str(item) for item in queryset]
        expectedRes = ['Pizza : 150.00', 'Hamburger : 100.00', 'LemonCake : 90.00']

        returnedRes.sort()
        expectedRes.sort()

        self.assertEqual(expectedRes, returnedRes)

        


            

