from django.db import models
from django.urls import reverse
# Create your models here.

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, blank=True,  verbose_name='姓名')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'account'

    @classmethod
    def is_exist_user(cls, username):
        """
        检查当前用户是否存在
        """
        return UserProfile.objects.filter(username=username).exists()
