from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    university = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to="account/", blank=True, null=True)