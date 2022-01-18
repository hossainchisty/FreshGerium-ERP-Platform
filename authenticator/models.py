from cloudinary.models import CloudinaryField

from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session
from django.db import models
from django.utils.timezone import now

from .manager import UserManager


class User(AbstractUser):
    """ Customize default User model """

    email = models.EmailField(unique=True)
    owner_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=11)
    organization_name = models.CharField(max_length=50)
    business = models.CharField(max_length=50)
    business_manager_name = models.CharField(max_length=50,  null=True, blank=True)
    brand_logo = CloudinaryField('Brand Logo', null=True, blank=True)
    otp = models.SmallIntegerField(null=True, blank=True)
    otp_created_time = models.DateTimeField(default=now, editable=False)
    token = models.CharField(max_length=100, unique=True)
    is_verified = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank=True, null=True)

    is_founder = models.BooleanField(default=False)
    is_ceo = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_head_office = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_auditor = models.BooleanField(default=False)
    is_auditor_manager = models.BooleanField(default=False)
    is_auditor_head_office = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=now, editable=False)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
