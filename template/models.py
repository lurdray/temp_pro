from django.db import models
from django.utils import timezone

from app_user.models import *

# Create your models here.


class Template(models.Model):
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    body = models.TextField()

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)