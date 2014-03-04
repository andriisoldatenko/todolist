from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from tasks.models import Task


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']

class TaskResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Task.objects.all()
        resource_name = 'entry'
