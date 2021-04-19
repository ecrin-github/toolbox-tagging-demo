from django.conf import settings
from django.db import models
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey


# Create your models here.
class ResourceType(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Resource types"


class ResearchField(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Research fields"


class SpecificTopic(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specific topics"


class GeographicalScope(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Geographical scope"


class CountryGrouping(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    geographical_scope = models.ForeignKey(GeographicalScope, on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries grouping"


class DataType(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Data Types"


class DataTypeSub(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Data types subgroups"


class StageInDS(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Stage in DS"


class Tag(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"


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
