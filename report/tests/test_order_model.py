from order.models import Order
from django.test import TestCase


class OrderModelTest(TestCase):
    ''' Test suite for order model '''

    def setUp(self):
        ''' Create a order instance for testing '''
        # TODO: Add product, customer, supplier.
        Order.objects.create()

    def tearDown(self):
        ''' Delete order instance after testing '''
        Order.objects.all().delete()
