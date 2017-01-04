from django.contrib import admin
from .models import Contact
from django.contrib.admin import ModelAdmin

class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'posted_on')


admin.site.register(Contact, ContactAdmin)
