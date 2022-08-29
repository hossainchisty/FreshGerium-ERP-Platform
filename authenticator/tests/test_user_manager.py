from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagersTests(TestCase):
    ''' Test suite for custom managers '''

    def test_create_user(self):
        ''' Create a instance for testing '''
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com',
            owner_name='Wota',mobile_number='015000000000',  password='foo'
        )
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.owner_name, 'Wota')
        self.assertEqual(user.mobile_number, '015000000000')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
