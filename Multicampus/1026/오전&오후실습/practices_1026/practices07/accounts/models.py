from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    profile_image = models.ImageField(upload_to="images/", blank=True)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"
