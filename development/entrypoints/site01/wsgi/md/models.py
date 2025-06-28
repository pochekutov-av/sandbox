from django.db import models


from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    ident = models.CharField(max_length=63, unique=True)
    email = models.CharField(max_length=128)

    USERNAME_FIELD = 'ident'
    EMAIL_FIELD = 'email'

    class Meta:
        db_table = 'users'
