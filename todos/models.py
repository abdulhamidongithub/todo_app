from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=(('new', 'new'), ('done', 'done')))
    time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} ({self.status})"