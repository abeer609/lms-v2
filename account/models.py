from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = [
    ("Teacher", "Teacher"),
    ("Student", "Student"),
]


class User(AbstractUser):
    role = models.CharField(choices=ROLES, max_length=20)
