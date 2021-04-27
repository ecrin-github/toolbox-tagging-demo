from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from resources.models import *
from tagging.models import TaggingResource
from app.admin import ExportCsvMixin


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin, ExportCsvMixin):
    exclude = ['added_by',]
    list_display = ("title", "creation_date", "update_date", "added_by")
    
    fields = [
        'title',
        'description',
        'url',
        'file',
        'tagging_persons',
        'creation_date',
        'update_date',
        'added_by',
        'resource_type',
        'research_field',
        'geographical_scope',
        'countries_grouping',
        'specific_topics',
        'data_type',
        'data_type_subtypes',
        'stage_in_data_sharing_life_cycle'
    ]

    readonly_fields = (
        'creation_date',
        'update_date',
        'added_by',
        'resource_type',
        'research_field',
        'geographical_scope',
        'countries_grouping',
        'specific_topics',
        'data_type',
        'data_type_subtypes',
        'stage_in_data_sharing_life_cycle',
    )

    actions = ["export_as_csv"]


    def resource_type(self, obj):
        tagging_resource = TaggingResource.objects.filter(resource=obj)
        if tagging_resource.exists():
            tagged_resource = TaggingResource.objects.get(resource=obj)
            resource_type = ''
            for res_type in tagged_resource.resource_type.all():
                resource_type += res_type.name + '\n'
            if resource_type != '':
                return resource_type
            else:
                return 'None'
        return 'None'
    

    def research_field(self, obj):
        tagging_resource = TaggingResource.objects.filter(resource=obj)
        if tagging_resource.exists():
            tagged_resource = TaggingResource.objects.get(resource=obj)
            research_field = ''
            for res_field in tagged_resource.research_field.all():
                research_field += res_field.name + '\n'
            if research_field != '':
                return research_field
            else:
                return 'None'
        return 'None'

    
    def geographical_scope(self, obj):
        tagging_resource = TaggingResource.objects.filter(resource=obj)
        if tagging_resource.exists():
            tagged_resource = TaggingResource.objects.get(resource=obj)
            if tagged_resource.geographical_scope is not None:
                return tagged_resource.geographical_scope.name
            else:
                return 'None'
        return 'None'

    
    def countries_grouping(self, obj):
        tagging_resource = TaggingResource.objects.filter(resource=obj)
        if tagging_resource.exists():
            tagged_resource = TaggingResource.objects.get(resource=obj)
            countries_grouping = ''
            for country in tagged_resource.country_grouping.all():
                countries_grouping += country.name + '\n'
            if countries_grouping != '':
                return countries_grouping
            else:
                return 'None'
        return 'None'


    def specific_topics(self, obj):
        tagging_resource = TaggingResource.objects.filter(resource=obj)
        if tagging_resource.exists():
            tagged_resource = TaggingResource.objects.get(resource=obj)
            specific_topic = ''
            for spec_topic in tagged_resource.specific_topic.all():
                specific_topic += spec_topic.name + '\n'
            if specific_topic != '':
                return specific_topic
            else:
                return 'None'
        return 'None'


    def data_type(self, obj):
        tagging_resource = TaggingResource.objects.filter(resource=obj)
        if tagging_resource.exists():
            tagged_resource = TaggingResource.objects.get(resource=obj)
            if tagged_resource.data_type is not None:
                return tagged_resource.data_type.name
            else:
                return 'None'
        return 'None'

    
    def data_type_subtypes(self, obj):
        tagging_resource = TaggingResource.objects.filter(resource=obj)
        if tagging_resource.exists():
            tagged_resource = TaggingResource.objects.get(resource=obj)
            data_type_subtypes = ''
            for data_types in tagged_resource.data_type_sub.all():
                data_type_subtypes += data_types.name + '\n'
            if data_type_subtypes != '':
                return data_type_subtypes
            else:
                return 'None'
        return 'None'


    def stage_in_data_sharing_life_cycle(self, obj):
        tagging_resource = TaggingResource.objects.filter(resource=obj)
        if tagging_resource.exists():
            tagged_resource = TaggingResource.objects.get(resource=obj)
            stage_in_ds = ''
            if tagged_resource.stage_in_ds is not None:
                return tagged_resource.stage_in_ds.name
            else:
                return 'None'
        return 'None'


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
        resource = Resource.objects.get(id=obj.pk)
        check_tagging_resource = TaggingResource.objects.filter(resource=resource)
        if not check_tagging_resource.exists():
            TaggingResource(resource=resource).save()            
