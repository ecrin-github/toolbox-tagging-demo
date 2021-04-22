from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



# Create your models here.
class Permission(Permission):
    pass


class Group(Group):
    pass


class User(AbstractUser):
    ADMINISTRATOR = 1
    CONTENT_MANAGER = 2
    TAGGING_MANAGER = 3

    ROLE_CHOICES = (
        (ADMINISTRATOR, 'Administrator'),
        (CONTENT_MANAGER, 'Content manager'),
        (TAGGING_MANAGER, 'Tagging manager')
    )
    
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    groups = models.ForeignKey(Group, blank=True, null=False, on_delete=models.CASCADE)


