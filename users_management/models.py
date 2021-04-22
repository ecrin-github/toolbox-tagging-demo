from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



# Create your models here.
class Permission(Permission):
    pass


class Group(Group):
    pass


class User(AbstractUser):
    groups = models.ForeignKey(Group, blank=False, null=False, on_delete=models.CASCADE, default=1)
