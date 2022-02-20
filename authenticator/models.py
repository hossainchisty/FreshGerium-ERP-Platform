from functools import cached_property

from cloudinary.models import CloudinaryField

from common.utils import INDUSTRYCHOICES
from django.contrib.auth.models import AbstractUser
# from django.contrib.gis.db import models
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
    business = models.CharField(max_length=50, choices=INDUSTRYCHOICES)
    business_manager_name = models.CharField(max_length=50,  null=True, blank=True)
    brand_logo = CloudinaryField('Brand Logo', null=True, blank=True)
    otp = models.SmallIntegerField(null=True, blank=True)
    otp_created_time = models.DateTimeField(default=now, editable=False)
    token = models.CharField(max_length=100, unique=True, null=True, blank=True, editable=False)
    is_verified = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    # location of the shop in latitude and longitude coordinates
    # location = models.PointField()
    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank=True, null=True)
    password_changes_datatime = models.DateTimeField(blank=True, null=True)
    login_datetime = models.DateTimeField(blank=True, null=True)
    logout_datetime = models.DateTimeField(blank=True, null=True)
    last_activity = models.DateTimeField(blank=True, null=True)
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

    @cached_property
    def get_brand_logo_url(self):
        if self.brand_logo and hasattr(self.brand_logo, 'url'):
            return self.brand_logo.url
        else:
            return "/static/images/avatar.jpg"

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
