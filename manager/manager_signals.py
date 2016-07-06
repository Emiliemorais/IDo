import django.dispatch
from notifications.models import Notification

notification_read = django.dispatch.Signal(providing_args=["notification_id"])

def mark_notification_as_read(sender, notification_id, **kwargs):
	notification = Notification.objects.get(id=notification_id)
	notification.mark_as_read()

notification_read.connect(mark_notification_as_read)
