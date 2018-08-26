from django.conf import settings
from django.db import models

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
