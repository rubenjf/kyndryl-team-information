from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

        