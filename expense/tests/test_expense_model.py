from django.test import TestCase
from expense.models import Category, Expense
from authenticator.models import User
from common.utils import INDUSTRYCHOICES


class CategoryModelTest(TestCase):
    ''' Test suite for Category model '''

    def setUp(self):
        ''' Create a expense/category instance for testing '''
        Category.objects.create(
            id=1,
            name="Rental cost",
        )

    def tearDown(self):
        ''' Delete expense/category instance after testing '''
        Category.objects.all().delete()

    def test_category_name(self):
        ''' Test category type '''
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, category.name)


class ExpenseModelTest(TestCase):
    ''' Test suite for Expense model '''

    def setUp(self):
        '''  Create a expense instance for testing '''

        user = User.objects.create(
           email='testMe@gmail.com',
           owner_name='Luke',
           mobile_number='+8982237131',
           organization_name='Meta Inc',
           business=INDUSTRYCHOICES[0],
           business_manager_name='Jon',
           otp=234671,
           is_verified=True,
        )

        try:
            category = Category.objects.get(id=1)
        except Category.DoesNotExist:
            category = None
            Expense.objects.create(
                id=1,
                user=user, # Just added user for signals sending email.
                category=category,
                date="2020-01-01",
                expense_type="Food",
                amount=10.00,
            )

        
    def tearDown(self):
        ''' Delete expense instance after testing '''
        Expense.objects.all().delete()
        Category.objects.all().delete()

    def test_expense_type(self):
        ''' Test expense type '''
        expense = Expense.objects.get(id=1)
        self.assertEqual(expense.expense_type, expense.expense_type)

    def test_expense_amount(self):
        ''' Test expense amount '''
        expense = Expense.objects.get(id=1)
        self.assertEqual(expense.amount, 10.00)
