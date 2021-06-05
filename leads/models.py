from django.db import models
from teams.models import Teams
from accounts.models import Account
from contacts.models import Contact
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Leads(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    data_of_birth = models.DateField(
    help_text='Please use the following format: <em>YYYY-MM-DD</em>.')

    LEADS_SOURCE = (
        ('Google','Google'),
        ('Facebook','Facebook'),
        ('Linkedin','Linkedin'),
    )
    source = models.CharField(max_length=200,blank=True,null=True, choices=LEADS_SOURCE)

    LEAD_ROLE = (
        ('Admin','Admin'),
        ('Lead Manager', 'Lead Manager'),
        ('Manager', 'Manager'),
    )

    assigned_to = models.CharField(help_text='Select A Staff Member',max_length=200,blank=True,null=True, choices=LEAD_ROLE)

    STATUS = (
        ('New','New'),
        ('Working','Working'),
        ('Contacted','Contacted'),
        ('Proposal Sent','Proposal Sent'),
        ('Qualified','Qualified'),
        ('Customer (Converted Lead)','Customer (Converted Lead)'),
        ('Others','Others'),
    )
    status = models.CharField(max_length=200, choices=STATUS)

    country = CountryField()
    zipcode = models.IntegerField(blank=True,null=True)

    website = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    contacts = models.ManyToManyField(Contact)
    teams = models.ManyToManyField(Teams)
    accounts_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Leads"

    def __str__(self):
        return self.full_name
        