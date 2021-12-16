from django.test import TestCase
from products.models import Category, Product, Unit
from suppliers.models import Supplier


class TestProductModel(TestCase):
    '''
    TODO:
    Test suite for Category, Product, Unit model
    '''

    def setUp(self):
        '''
        Create a  instance for testing
        '''
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

        Unit.objects.create(
            name='Kilogram', status=True
        )

        category = Category.objects.create(
            name='Test Category',
            is_active=True,
        )

        Product.objects.create(
            product_name='Test Product',
            product_description='Test Product Description',
            product_model='Test Product Model',
            price=100.90,
            supplier_price=90.90,
            unit=('kg', 'Kilogram'),
            category=category,
            supplier=supplier,
        )

    def tearDown(self):
        '''
        Delete instance after testing
        '''
        Product.objects.all().delete()
        Category.objects.all().delete()
        Unit.objects.all().delete()
        Supplier.objects.all().delete()

    def test_product_name(self):
        ''' Test case for product name is created '''
        product = Product.objects.get(product_name='Test Product')
        self.assertEqual(product.product_name, 'Test Product')
