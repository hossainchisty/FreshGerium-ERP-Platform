from django.test import TestCase
from products.models import Category, Product, Unit
from suppliers.tests.test_suppliers_model import supplier


class TestProductModel(TestCase):
    ''' Test suite for Category, Product, Unit model '''

    def setUp(self):
        ''' Create a instance for testing '''

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
            in_stock=200,
            supplier_price=90.90,
            unit=Unit.objects.get(id=1),
            category=category,
            supplier=supplier,
        )

    def tearDown(self):
        ''' Delete instance after testing '''
        Product.objects.all().delete()
        Category.objects.all().delete()
        Unit.objects.all().delete()

    def test_unit_name(self):
        ''' Test case unit name '''
        unit = Unit.objects.get(name='Kilogram')
        self.assertTrue(unit.name)

    def test_unit_status(self):
        ''' Test case unit status check '''
        unit = Unit.objects.get(name='Kilogram')
        self.assertTrue(unit.status)

    def test_category_name(self):
        ''' Test case for category '''
        category = Category.objects.get(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

    def test_category_isActive(self):
        ''' Test case for category is active '''
        category = Category.objects.get(name='Test Category')
        self.assertTrue(category.is_active)

    def test_product_name(self):
        ''' Test case for product name is created '''
        product = Product.objects.get(product_name='Test Product')
        self.assertEqual(product.product_name, product.product_name)

    def test_product_description(self):
        ''' Test case for product desc '''
        product = Product.objects.get(product_name='Test Product')
        self.assertEqual(product.product_description, 'Test Product Description')

    def test_product_model(self):
        ''' Test case for product model '''
        product = Product.objects.get(product_name='Test Product')
        self.assertEqual(product.product_model, 'Test Product Model')

    def test_product_price(self):
        ''' Test case for product price '''
        product = Product.objects.get(product_name='Test Product')
        self.assertEqual(product.price, product.price)

    def test_product_price_not_same(self):
        ''' Test case for product price not same '''
        product = Product.objects.get(product_name='Test Product')
        self.assertNotEqual(product.price, 100.20)

    def test_product_stock(self):
        ''' Test case for product stock '''
        product = Product.objects.get(product_name='Test Product')
        self.assertTrue(product.in_stock, 200)

    def test_product_stock_out(self):
        ''' Test case for product stock out '''
        product = Product.objects.get(product_name='Test Product')
        self.assertNotEqual(product.in_stock, 300)
