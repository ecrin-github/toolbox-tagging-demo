from django.db import models
from django.conf import settings

from users_management.models import User


# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/', max_length=350, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tagging_persons = models.ManyToManyField(User, unique=False, blank=False, related_name='tagging_persons')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, unique=False, related_name='added_by')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Resources"
