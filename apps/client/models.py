from django.contrib.auth.models import User
from django.db import models
from django. utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company_number = models.CharField(max_length=255, blank=True, null=True)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    state_name = models.CharField(max_length=50, blank=True, null=True)
    country_name = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    contact_reference = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        User, related_name='clients', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name
