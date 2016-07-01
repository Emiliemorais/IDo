from notifications.signals import notify
from models import Message
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import Group

def message_notify(sender, instance, created, **kwargs):
	group = Group.objects.get(name="admin")
	notify.send(instance, recipient=group, verb=_('send a new message'), description='new message')

def budget_notify(sender, instance, created, **kwargs):
	group = Group.objects.get(name="admin")
	notify.send(instance, recipient=group, verb=_('solicited a budget'), description='new solicited budget')

