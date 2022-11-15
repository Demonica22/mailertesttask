from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_info(self):
        info = [f"First name: {self.first_name}",
                f"Last name: {self.last_name}",
                f"Email: {self.email}",
                f"Date of birth: {self.birth_date}"]
        return info
