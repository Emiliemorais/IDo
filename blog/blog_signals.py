from notifications.signals import notify
from models import Message
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import Group

def my_notify(sender, instance, created, **kwargs):
	group = Group.objects.get(name="admin")
	notify.send(instance, recipient=group, verb=_('new message'))