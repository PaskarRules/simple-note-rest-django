from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from .validators import email_validator, password_validate, first_name_validate, last_name_validate


class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None):
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name=None, last_name=None, ):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser):
    email = models.CharField(verbose_name='email address', max_length=255, unique=True, validators=[email_validator])
    first_name = models.CharField(max_length=40, validators=[first_name_validate], blank=True, null=True)
    last_name = models.CharField(max_length=40, validators=[last_name_validate], blank=True, null=True)
    password = models.CharField(max_length=40, validators=[password_validate])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "auth_user"
