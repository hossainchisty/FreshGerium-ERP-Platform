from damage.models import Damage
from django.test import TestCase
from products.tests.test_product_model import product
from suppliers.tests.test_suppliers_model import supplier


class DamageModelTest(TestCase):
    ''' Test suite for damage model '''

    def setUp(self):
        ''' Create a damage instance for testing '''
        # TODO: Add product, customer, supplier.
        Damage.objects.create()

    def tearDown(self):
        ''' Delete damage instance after testing '''
        Damage.objects.all().delete()
