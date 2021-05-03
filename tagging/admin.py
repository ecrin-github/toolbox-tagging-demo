from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from django.utils.safestring import mark_safe

from tagging.models import *
from general.configs import HOST


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
                'created',
                'updated',
                'added_by',
                'current_status',
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
        'created',
        'updated',
        'added_by',
        'current_status',
    )


    def description(self, obj):
        if obj.resource.description is not None and obj.resource.description != '':
            return obj.resource.description
        return 'None'


    def url(self, obj):
        if obj.resource.url is not None and obj.resource.url != '':
            url = '<a href="{}" target="_blank">{}</a>'.format(obj.resource.url, obj.resource.url)
            return mark_safe(url)
        return 'None'


    def attached_file(self, obj):
        if obj.resource.resource_file is not None and obj.resource.resource_file != '':
            url = '<a href="{}{}" target="_blank">File</a>'.format(HOST, obj.resource.resource_file)
            return mark_safe(url)
        return 'None'


    def created(self, obj):
        if obj.resource.created is not None and obj.resource.created != '':
            return obj.resource.created
        return 'None'


    def updated(self, obj):
        if obj.resource.updated is not None and obj.resource.updated != '':
            return obj.resource.updated
        return 'None'


    def current_status(self, obj):
        if obj.resource.current_status is not None and obj.resource.current_status != '':
            return obj.resource.current_status
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
