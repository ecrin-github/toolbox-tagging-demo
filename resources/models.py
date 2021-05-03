from django.db import models
from django.conf import settings

from users_management.models import TaggingUser


# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=1000, null=False, blank=False)
    resource_file = models.FileField(upload_to='uploads/', max_length=450, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tagging_persons = models.ManyToManyField(TaggingUser, unique=False, blank=False, related_name='tagging_persons')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, unique=False, related_name='added_by')
    current_status = models.CharField(max_length=75, null=False, blank=True, default='Waiting for tagging')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Resources"
