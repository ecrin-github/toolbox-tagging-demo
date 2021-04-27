from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from tagging.models import *


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
@admin.register(TaggingResource)
class TaggingResourceAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Bibliographic data', {
            "fields": (
                'resource',
                'description',
                'url',
                'attached_file',
            ),
        }),
        ('Additional data', {
            "fields": (
                'creation_date',
                'update_date',
                'added_by',
            ),
        }),
        ('Tagging data', {
            "fields": (
                'resource_type',
                'research_field',
                'data_type',
                'data_type_subs',
                'stage_in_ds',
                'geographical_scope',
                'countries_grouping',
                'specific_topics',
            ),
        }),
    )

    readonly_fields = (
        'resource',
        'description',
        'url',
        'attached_file',
        'creation_date',
        'update_date',
        'added_by',
    )


    def description(self, obj):
        if obj.resource.description is not None and obj.resource.description != '':
            return obj.resource.description
        return 'None'


    def url(self, obj):
        if obj.resource.url is not None and obj.resource.url != '':
            return obj.resource.url
        return 'None'


    def attached_file(self, obj):
        if obj.resource.file is not None and obj.resource.file != '':
            return obj.resource.file
        return 'None'


    def creation_date(self, obj):
        if obj.resource.creation_date is not None and obj.resource.creation_date != '':
            return obj.resource.creation_date
        return 'None'


    def update_date(self, obj):
        if obj.resource.update_date is not None and obj.resource.update_date != '':
            return obj.resource.update_date
        return 'None'


    def added_by(self, obj):
        if obj.resource.added_by is not None and obj.resource.added_by != '':
            return obj.resource.added_by
        return 'None'


    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='assign_categories')
            if perms.exists():
                return True
            return False
        except:
            pass

    @csrf_protected_method
    def has_add_permission(self, request):
        return False

    
    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='assign_categories')
        user_check = Resource.objects.filter(tagging_persons=request.user.id)
        if perms.exists() and user_check.exists():
            return True
        return False

    
    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    
    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        return False

    
    @csrf_protected_method
    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)
