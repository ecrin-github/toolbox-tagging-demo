from django.contrib import admin
from app.models import *
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


csrf_protected_method = method_decorator(csrf_protect)


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
class ResourceAdmin(admin.ModelAdmin):
    exclude = ['added_by',]

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
