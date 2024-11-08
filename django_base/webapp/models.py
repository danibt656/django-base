from django.contrib.auth.models import AbstractUser
from django.db import models


# Organisation model
class Organisation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Custom user model
class CustomUser(AbstractUser):
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True, blank=True
    )
