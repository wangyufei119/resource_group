from django.db import models
from account.models import UserProfile


# Create your models here.

class CustomGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, verbose_name='群组名称')
    manager_list = models.CharField(max_length=255, blank=True, verbose_name='群组管理员列表')

    class Meta:
        db_table = 'custom_group'


class GroupUserMap(models.Model):
    """
    群组映射表
    """
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'custom_group_user_map'

