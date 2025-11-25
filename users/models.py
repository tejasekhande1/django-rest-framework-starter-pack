from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import AbstractBaseModel
from users.enums import UserRoles
from users.managers import UserManager


class User(AbstractUser, AbstractBaseModel):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(
        max_length=255,
        choices=UserRoles.choices,
        null=False,
    )

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()
