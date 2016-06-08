from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    
    sender_name = models.CharField(max_length=100)
    customer_email = models.EmailField(blank=True)
    phone_email = models.CharField(max_length=12, blank=True)
    content = models.TextField()
    
    def __str__(self):
        return self.sender_name

        
