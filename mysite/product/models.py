from django.db import models

from group.models import CustomGroup


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, verbose_name='产品名称')
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
