from django.db import models
from django.conf import settings

from users_management.models import TaggingUser


# Create your models here.
class ResourceType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Resource types'



class Language(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Languages'


class Resource(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    short_title = models.CharField(max_length=250, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    authors = models.TextField(null=False, blank=False, default='Unknown')
    year_of_publication = models.IntegerField(null=False, blank=False, default=1950)
    doi = models.CharField(max_length=175, null=True, blank=True, verbose_name='DOI')
    language = models.ForeignKey(Language, unique=False, on_delete=models.CASCADE, null=True, blank=True)
    type_of_resource = models.ForeignKey(ResourceType, unique=False, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(max_length=1000, null=False, blank=False, verbose_name='URL')
    resource_file = models.FileField(upload_to='uploads/', max_length=450, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tagging_persons = models.ManyToManyField(TaggingUser, unique=False, blank=True, related_name='tagging_persons')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, unique=False, related_name='added_by')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Resources"



class ResourceStatus(models.Model):
    resource = models.OneToOneField(Resource, unique=False, null=True, on_delete=models.CASCADE)
    waiting_for_tagging = models.BooleanField(null=False, blank=True, default=False)
    is_tagged = models.BooleanField(null=False, blank=True, default=False)
    waiting_for_approval = models.BooleanField(null=False, blank=True, default=False)
    is_approved = models.BooleanField(null=False, blank=True, default=False)
    status_description = models.CharField(max_length=75, null=False, blank=True, default='None')

    class Meta:
        verbose_name_plural = "Resources statuses"
