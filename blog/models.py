from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

class Message(models.Model):
    
    sender_name = models.CharField((_('Sender name')), max_length=100)
    customer_email = models.EmailField((_('Customer email')), blank=True)
    phone_email = models.CharField((_('Phone email')), max_length=12, blank=True)
    content = models.TextField((_('Message')))
    
    def __str__(self):
        return self.sender_name


class Questionnaire(models.Model):

    DAY = _('Days')
    WEEK = _('Weeks')
    MONTH = _('Months')
    YEAR = _('Years')

    DATE_PERIOD =  (
    (DAY, _('Days')),
    (WEEK, _('Weeks')),
    (MONTH, _('Months')),
    (YEAR, _('Years')),
    )
    
    SPORTING =  _('Sporting')
    ADVENTUROUS =  _('Adventurous')
    HOMELIKE = _('Homelike')
    PARTIER = _('Partier')
    FITNESS = _('Fitness')

    LIFESTYLE = (
    (SPORTING, _('Sporting')),
    (ADVENTUROUS, _('Adventurous')),
    (HOMELIKE, _('Homelike')),
    (PARTIER, _('Partier')),
    (FITNESS, _('Fitness')),
    )

    sender_name = models.CharField((_('Sender name')), max_length=100)
    sender_age = models.IntegerField((_('Sender age')))
    partner_name = models.CharField((_('Partner name')), max_length=100)
    partner_age = models.IntegerField((_('Partner age')))
    story = models.TextField((_('Story')), blank=True)
    relationship_time_number = models.IntegerField((_('Relationship time number')), blank=True, default=0)
    relationship_time = models.CharField((_('Date Period')), choices=DATE_PERIOD, max_length=100, blank=True)
    lifestyle = models.CharField((_('Lifestyle')), choices=LIFESTYLE, blank=True,  max_length=100)
    personality = models.CharField((_('Personality')), max_length=100)
    cost_pretension = models.IntegerField((_('Cost pretension')), blank=True, default=0)
    ideal_place = models.CharField((_('Ideal place')),  max_length=100)
    sender_email = models.EmailField((_('Sender email')))
    sender_phone = models.CharField((_('Sender phone')), max_length=12, blank=True)
    additional_info = models.TextField((_('Additionl info')), blank=True)
    
    def __str__(self):
        return self.sender_name

           
