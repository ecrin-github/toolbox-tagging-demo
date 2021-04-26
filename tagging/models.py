from django.db import models
from django.conf import settings
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey

from categories.models import ResourceType, ResearchField, SpecificTopic, \
    GeographicalScope, CountryGrouping, DataType, DataTypeSub, StageInDS
from users_management.models import User
from resources.models import Resource


# Create your models here.
class TaggingResource(models.Model):
    resource = models.ForeignKey(Resource, unique=False, null=False, default=0, on_delete=models.CASCADE)
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
    stage_in_ds = models.ForeignKey(StageInDS, unique=False, verbose_name='Stage in data sharing life cycle', on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.resource.title

    class Meta:
        verbose_name_plural = "Waiting for tagging"
