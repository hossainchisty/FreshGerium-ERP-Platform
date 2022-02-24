from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        '''String for representing the Model object.'''
        return self.name
