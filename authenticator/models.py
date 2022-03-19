from functools import cached_property

from cloudinary.models import CloudinaryField

from common.utils import INDUSTRYCHOICES
from django.contrib.auth.models import AbstractUser
# from django.contrib.gis.db import models
from django.contrib.sessions.models import Session
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

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

    otp = models.SmallIntegerField(
        help_text='One Time Password',
        null=True, blank=True
    )
    token = models.CharField(
        max_length=100,
        unique=True,
        null=True, blank=True, editable=False,
        help_text='Token for authentication'
    )
    ip_address = models.GenericIPAddressField(
        help_text='IP Address',
        blank=True, null=True
    )
    # TODO: Add geographical location with django-gis
    ''' location of the shop in latitude and longitude coordinates '''
    # location = models.PointField()

    is_verified = models.BooleanField(
        _('verified'),
        default=False,
        help_text=_(
            'Designates whether this user has been verified.'
            'Un-verified users cannot log in.'
        ),
    )
    is_founder = models.BooleanField(
        _('founder'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as founder.'
        ),
    )
    is_ceo = models.BooleanField(
        _('ceo'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as CEO.'
        ),
    )
    is_admin = models.BooleanField(
        _('admin'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as admin.'
        ),
    )
    is_manager = models.BooleanField(
        _('manager'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as manager.'
        ),
    )
    is_head_office = models.BooleanField(
        _('head office'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as head office.'
        ),
    )
    is_hr = models.BooleanField(
        _('hr'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as Human resources (HR).'
        ),
    )
    is_accountant = models.BooleanField(
        _('accountant'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as accountant.'
        ),
    )
    is_auditor = models.BooleanField(
        _('auditor'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as auditor.'
        ),

    )
    is_auditor_manager = models.BooleanField(
        _('auditor manager'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as auditor manager.'
        ),
    )
    is_auditor_head_office = models.BooleanField(
        _('auditor head office'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as auditor head office.'
        ),
    )
    is_employee = models.BooleanField(
        _('employee'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as employee.'
        ),
    )
    is_customer = models.BooleanField(
        _('customer'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as customer.'
        ),
    )
    is_supplier = models.BooleanField(
        _('supplier'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as supplier.'
        ),
    )

    # Timestamps fields
    otp_created_time = models.DateTimeField(default=now, editable=False)
    password_changes_datatime = models.DateTimeField(blank=True, null=True)
    login_datetime = models.DateTimeField(blank=True, null=True)
    logout_datetime = models.DateTimeField(blank=True, null=True)
    last_activity = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=now, editable=False)

    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank=True, null=True)

    # TODO: eXtract username from email address.
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
