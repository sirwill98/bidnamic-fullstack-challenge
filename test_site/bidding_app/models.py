from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class ClientApplicationData(models.Model):
    class TITLE_OPTIONS(models.TextChoices):
        MR = 'Mr', _('Mr')
        MRS = 'Mrs', _('Mrs')
        MISS = 'Miss', _('Miss')
        MS = 'Ms', _('Ms')
        OTHER = 'Other', _('Other')

    class BIDDING_SETTING(models.TextChoices):
        HIGH = 'High', _('High')
        MEDIUM = 'Medium', _('Medium')
        LOW = 'Low', _('Low')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=5, choices=TITLE_OPTIONS.choices)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    company_name = models.CharField(max_length=128)
    address = models.TextField()
    telephone = PhoneNumberField()
    bidding_settings = models.CharField(max_length=6, choices=BIDDING_SETTING.choices)
    google_ads_account_id = models.CharField(max_length=10) # needs validated
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.first_name}"