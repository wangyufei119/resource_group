from django.contrib import admin
from group.models import CustomGroup, GroupUserMap

# Register your models here.
admin.site.register(CustomGroup)
admin.site.register(GroupUserMap)
