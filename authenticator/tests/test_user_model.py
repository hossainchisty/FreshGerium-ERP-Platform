from django.test import TestCase
from common.utils import INDUSTRYCHOICES
from authenticator.models import User

class TestUserModel(TestCase):
    ''' Test suite for User models '''

    def setUp(self):
        ''' Create a instance for testing '''

        User.objects.create(
           email='testMe@gmail.com',
           owner_name='Luke',
           mobile_number='+8982237131',
           organization_name='Meta Inc',
           business=INDUSTRYCHOICES[0],
           business_manager_name='Jon',
           otp=234671,
           is_verified=True,
        )

    def tearDown(self):
        ''' Delete instance after testing '''
        User.objects.all().delete()


    def test_user_email(self):
        ''' Test case for email '''
        user = User.objects.get(email='testMe@gmail.com')
        self.assertTrue(user.email)
    
    def test_owner_name(self):
        ''' Test case for owner '''
        user = User.objects.get(email='testMe@gmail.com')
        self.assertTrue(user.owner_name)    
        
    def test_mobile_number(self):
        ''' Test case for mobile number '''
        user = User.objects.get(email='testMe@gmail.com')
        self.assertTrue(user.mobile_number)
        
    def test_organization_name(self):
        ''' Test case for organization name'''
        user = User.objects.get(email='testMe@gmail.com')
        self.assertTrue(user.organization_name)    
        
    def test_business_type(self):
        ''' Test case for business type '''
        user = User.objects.get(email='testMe@gmail.com')
        self.assertTrue(user.business)    
        
    def test_manager_name(self):
        ''' Test case for manager name '''
        user = User.objects.get(email='testMe@gmail.com')
        self.assertEqual(user.business_manager_name, 'Jon')    
        
    def test_one_time_password(self):
        ''' Test case for OTP '''
        user = User.objects.get(email='testMe@gmail.com')
        self.assertEqual(user.otp, 234671)    
        
    def test_is_verified(self):
        ''' Test case for OTP '''
        user = User.objects.get(email='testMe@gmail.com')
        self.assertTrue(user.is_verified)
