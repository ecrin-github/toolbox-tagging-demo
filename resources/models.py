from django.db import models
from django.conf import settings
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey

from tagging.models import Tag
from categories.models import ResourceType, ResearchField, SpecificTopic, \
    GeographicalScope, CountryGrouping, DataType, DataTypeSub, StageInDS


# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    resource_type = models.ManyToManyField(ResourceType, unique=False)
    research_field = models.ManyToManyField(ResearchField, unique=False)
    geographical_scope = models.ForeignKey(GeographicalScope, default=1, on_delete=models.SET_NULL, null=True)
    country_grouping = ChainedManyToManyField(
        CountryGrouping,
        chained_field="geographical_scope",
        chained_model_field="geographical_scope",
        horizontal=True,
        verbose_name="Countries grouping"
    )
    specific_topic = models.ManyToManyField(SpecificTopic, unique=False)
    data_type = models.ForeignKey(DataType, default=1, on_delete=models.SET_NULL, null=True)
    data_type_sub = ChainedManyToManyField(
        DataTypeSub,
        chained_field="data_type",
        chained_model_field="data_type",
        horizontal=True,
        verbose_name="Data type subgroups"
    )
    stage_in_ds = models.ManyToManyField(StageInDS, unique=False)
    tags = models.ManyToManyField(Tag, unique=False)
    url = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/', max_length=350, null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, unique=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Resources"
