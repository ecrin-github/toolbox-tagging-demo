from django.db import models
from resources.models import Resource
from tagging.models import Tag


# Create your models here.
class WaitingResource(models.Model):
    resource = models.ForeignKey(Resource, unique=False, null=False, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, unique=False, blank=False)

    def __str__(self):
        return self.resource.title
    
    class Meta:
        verbose_name_plural = "Waiting for tagging"
