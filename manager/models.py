from __future__ import unicode_literals

from django.db import models

class Enterprise(models.Model):

    name = models.CharField(max_length=10)
    who = models.TextField()
    phone_contact = models.CharField(max_length=12)
    email_contact = models.EmailField()
    address = models.TextField()
    
    def __str__(self):
        return self.name
