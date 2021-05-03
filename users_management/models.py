from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



# Create your models here.
class User(AbstractUser):
    groups = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Users'


class ProjectCoordinator(User):
    class Meta:
        verbose_name_plural = "1. Project coordinators"


class ContentManager(User):
    class Meta:
        verbose_name_plural = "2. Content managers"


class TaggingUser(User):
    class Meta:
        verbose_name_plural = "3. Tagging users"
