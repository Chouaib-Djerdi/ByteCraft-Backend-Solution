from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    completed = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add=True)
