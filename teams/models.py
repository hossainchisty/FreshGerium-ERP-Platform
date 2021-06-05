from django.db import models
from django.contrib.auth.models import User

class Teams(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,null=True,blank=True, related_name="teams_created", on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name_plural = "Teams"
        ordering = ['-id',]

    def __str__(self):
        return self.name

