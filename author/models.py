from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)
    bio = models.TextField(max_length=200, blank=True, default="Bio")
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.username} Profile"
