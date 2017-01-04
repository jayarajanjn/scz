from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.db import models
import datetime

# Create your models here
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name="Name" )
    email = models.EmailField(blank=False, verbose_name="Email id")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], blank=True, max_length=12)
    #phonenumber = PhoneNumberField(blank=True, verbose_name="Phone Number")
    message = models.TextField(blank=False, verbose_name="Message")
    posted_on = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def __str__(self):
        return "{name} said: {message}".format(name=self.name,
                                           message=self.message
                                           )
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ["-posted_on"]
