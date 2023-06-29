from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Todo(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=CASCADE)
    done = models.BooleanField(default=False)