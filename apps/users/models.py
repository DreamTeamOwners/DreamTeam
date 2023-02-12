from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    second_name = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.user}'
