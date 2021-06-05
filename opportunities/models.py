from django.db import models
from teams.models import Teams
from contacts.models import Contact
from accounts.models import Account
from django.contrib.auth.models import User

class Opportunity(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of Opportunity:')
    Opportunities_description = models.TextField(verbose_name='Description')
    closed_on = models.DateField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    closed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contacts = models.ManyToManyField(Contact)
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Teams)

    class Meta:
        verbose_name_plural = "Opportunity"


    def __str__(self):
        return str(self.accounts)