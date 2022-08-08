from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	auth_code = models.CharField(max_length=20, default="null")

	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.user.username)

