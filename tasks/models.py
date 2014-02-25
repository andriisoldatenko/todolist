from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=20, blank=False)
    notes = models.CharField(max_length=200)
    priority = models.CharField(max_length=10)
    status = models.CharField(max_length=10)


class TaskList(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)