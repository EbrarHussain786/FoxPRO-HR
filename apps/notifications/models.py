from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=120)
    message = models.TextField()
    recipient_role = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
