from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from resources.models import *
from users_management.models import User
from tagging.models import TaggingResource
from app.admin import ExportCsvMixin


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
class TaggingResourceInline(admin.StackedInline):
    model = TaggingResource
    can_delete = False
    verbose_name_plural = 'Tagging data'
    fk_name = 'resource'



@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin, ExportCsvMixin):
    # exclude = ['added_by',]
    inlines = (TaggingResourceInline, )
    list_display = ("title", "created", "updated", "added_by",)
    
    fieldsets = (
        ('Bibliographic data', {
            "fields": (
                'title',
                'description',
                'url',
                'resource_file',
            ),
        }),
        ('Additional data', {
            "fields": (
                'tagging_persons',
                'created',
                'updated',
                'added_by',
                'current_status',
            ),
        })
    )

    readonly_fields = (
        'current_status',
        'created',
        'updated',
        'added_by',
    )

    actions = ["export_as_csv"]


    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if obj is not None:
            model_obj = self.model.objects.get(id=obj.id)
            if model_obj.added_by == request.user:
                context['adminform'].form.fields['tagging_persons'].queryset = User.objects.filter(groups__name='Tagging group')
                return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)
            else:
                return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)
        context['adminform'].form.fields['tagging_persons'].queryset = User.objects.filter(groups__name='Tagging group')
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)


    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_resources')
            if perms.exists():
                return True
            return False
        except:
            pass
    

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_resources')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_resources')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        if obj is not None:
            perms = request.user.groups.permissions.filter(codename='edit_resources')
            if perms.exists():
                model_obj = self.model.objects.get(id=obj.id)
                if model_obj.added_by == request.user:
                    return True
                else:
                    return False
            else:
                return False
        return False


    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            perms = request.user.groups.permissions.filter(codename='remove_resources')
            if perms.exists():
                model_obj = self.model.objects.get(id=obj.id)
                if model_obj.added_by == request.user:
                    return True
                else:
                    return False
            else:
                return False
        return False

    
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
        #resource = Resource.objects.get(id=obj.pk)
        #check_tagging_resource = TaggingResource.objects.filter(resource=resource)
        #if not check_tagging_resource.exists():
        #    TaggingResource(resource=resource).save()            
