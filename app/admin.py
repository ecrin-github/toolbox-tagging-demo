from django.contrib import admin
from app.models import *
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import csv
from django.http import HttpResponse
import datetime
from itertools import chain


csrf_protected_method = method_decorator(csrf_protect)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field for field in meta.fields]
        many_to_many_field_names = set([many_to_many_field for many_to_many_field in meta.many_to_many])
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(list(chain([str(field.verbose_name).capitalize() for field in field_names], [str(many_to_many_field.verbose_name).capitalize() for many_to_many_field in many_to_many_field_names])))
        for obj in queryset:
            row = []
            for field in field_names:
                value = getattr(obj, field.name)
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                row.append(value)
            for field in many_to_many_field_names:
                values = getattr(obj, field.name).all().values_list('name', flat=True)
                result_string = ""
                if values:
                    if len(values) > 1:
                        for val in values:
                            result_string += val + "; "
                        row.append(result_string)
                    elif len(values) == 1:
                        result_string = values[0]                        
                        row.append(result_string)
                else:
                    row.append(result_string)
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Export Selected"


# Register your models here.
@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ResearchField)
class ResearchFieldAdmin(admin.ModelAdmin):
    pass


class CountryGroupingInline(admin.TabularInline):
    model = CountryGrouping


@admin.register(GeographicalScope)
class GeographicalScopeAdmin(admin.ModelAdmin):
    inlines = [
        CountryGroupingInline
    ]


@admin.register(CountryGrouping)
class CountryGroupingAdmin(admin.ModelAdmin):
    pass


class DataTypeSubInline(admin.TabularInline):
    model = DataTypeSub


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    inlines = [
        DataTypeSubInline
    ]


@admin.register(DataTypeSub)
class DataTypeSubAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecificTopic)
class SpecificTopicAdmin(admin.ModelAdmin):
    pass


@admin.register(StageInDS)
class StageInDSAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin, ExportCsvMixin):
    exclude = ['added_by',]
    list_display = ("title", "creation_date", "update_date")
    actions = ["export_as_csv"]

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        if obj is not None:
            model_obj = self.model.objects.get(id=obj.id)
            if model_obj.added_by == request.user:
                return True
            else:
                return False
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            model_obj = self.model.objects.get(id=obj.id)
            if model_obj.added_by == request.user:
                return True
            else:
                return False
        return False

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
