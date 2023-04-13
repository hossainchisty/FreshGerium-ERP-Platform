from django.test import TestCase
from suppliers.models import Supplier


class TestSupplierModel(TestCase):
    ''' Test suite for Supplier model '''

    def setUp(self):
        ''' Create a instance for testing '''
        global supplier
        supplier = Supplier.objects.create(
            supplier_full_name='Test Supplier',
            supplier_address='Test Address',
            supplier_phone='+254712345678',
            supplier_email='testsupplier@gmail.com',
            supplier_zip_code='12345',
            supplier_country='Bangadesh',
            supplier_fax='+254712345678',
            supplier_previous_balance=23.00,
        )

    def tearDown(self):
        ''' Delete instance after testing '''
        Supplier.objects.all().delete()
