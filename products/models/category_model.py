from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
