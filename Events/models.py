from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Event(models.Model):
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_and_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} ({self.user.username})"