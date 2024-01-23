from django.db import models
from datetime import date

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True, blank=True)