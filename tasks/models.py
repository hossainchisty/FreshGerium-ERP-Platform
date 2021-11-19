from django.db import models
from teams.models import Teams
from accounts.models import Account
from contacts.models import Contact
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS_CHOICES = (
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )

    PRIORITY_CHOICES = (("Low", "Low"), ("Medium", "Medium"), ("High", "High"))

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    due_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True,null=True)

    account = models.ForeignKey(Account, null=True,blank=True,on_delete=models.SET_NULL)
    contact =  models.ManyToManyField(Contact)
    assigned_to = models.ManyToManyField(User)
    teams = models.ManyToManyField(Teams)

    class Meta:
        verbose_name_plural = "Tasks"
        ordering = ('-due_date',)

    def __str__(self):
        return self.title 