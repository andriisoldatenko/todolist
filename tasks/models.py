from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=20, blank=False)
    priority = models.CharField(max_length=10)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title