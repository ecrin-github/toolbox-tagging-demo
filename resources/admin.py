from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from resources.forms import NonRequiredInlineFormSet

from resources.models import Resource, ResourceStatus, Language
from users_management.models import User
from tagging.models import TaggingResource
# from app.admin import ExportCsvMixin


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
class TaggingResourceInline(admin.StackedInline):
    model = TaggingResource
    can_delete = False
    verbose_name_plural = 'Tagging data'
    fk_name = 'resource'
    formset = NonRequiredInlineFormSet
    formset_required = False
    extra = 1
    max_num = 1


    def get_readonly_fields(self, request, obj=None):
        if obj:
            check_resource_status = ResourceStatus.objects.filter(resource=obj)
            if check_resource_status.exists():
                resource_status = ResourceStatus.objects.get(resource=obj)
                if (resource_status.is_tagged == True and obj.added_by == request.user) or request.user.groups.name == 'Project coordinators':
                    return []
                else:
                    return [
                        "resource_type",
                        "research_field",
                        "geographical_scope",
                        "countries_grouping",
                        "specific_topics",
                        "data_type",
                        "data_type_subs",
                        "stage_in_ds",
                    ]
            else:
                return [
                "resource_type",
                "research_field",
                "geographical_scope",
                "countries_grouping",
                "specific_topics",
                "data_type",
                "data_type_subs",
                "stage_in_ds",
            ]
        else:
            return [
                "resource_type",
                "research_field",
                "geographical_scope",
                "countries_grouping",
                "specific_topics",
                "data_type",
                "data_type_subs",
                "stage_in_ds",
            ]


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    change_form_template = 'resources/change_resource.html'

    inlines = (TaggingResourceInline, )
    list_display = ("title", "created", "updated", "added_by", "current_status",)
    
    fieldsets = (
        ('Bibliographic data', {
            "fields": (
                'title',
                'short_title',
                'abstract',
                'authors',
                'year_of_publication',
                'doi',
                'language',
                'type_of_resource',
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
        'created',
        'updated',
        'added_by',
        'current_status',
    )

    actions = ["export_as_csv"]


    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['is_disabled'] = True
        extra_context['is_author'] = True
        return super().add_view(request, form_url=form_url, extra_context=extra_context)


    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        resource_status = ResourceStatus.objects.get(resource__id=object_id)
        if resource_status.waiting_for_approval:
            extra_context['is_disabled'] = False
        else:
            extra_context['is_disabled'] = True
        resource = Resource.objects.get(id=object_id)
        if resource.added_by == request.user:
            extra_context['is_author'] = True
        else:
            extra_context['is_author'] = False
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)


    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': False,
            'show_save_and_add_another': False
        })
        if obj is not None:
            model_obj = self.model.objects.get(id=obj.id)
            if model_obj.added_by == request.user:
                context['adminform'].form.fields['tagging_persons'].queryset = User.objects.filter(groups__name='Tagging group')
                context['adminform'].form.fields['language'].queryset = Language.objects.all().order_by('name')
                return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)
            else:
                return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)
        context['adminform'].form.fields['tagging_persons'].queryset = User.objects.filter(groups__name='Tagging group')
        context['adminform'].form.fields['language'].queryset = Language.objects.all().order_by('name')
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)


    def response_change(self, request, obj):
        
        if "_save" in request.POST:
            if obj.added_by is None or obj.added_by == '':
                obj.added_by = request.user
            resource = Resource.objects.get(id=obj.pk)

            check_tagging_resource = TaggingResource.objects.filter(resource=resource)
            if not check_tagging_resource.exists():
                TaggingResource(resource=resource).save()

            check_resource_status = ResourceStatus.objects.filter(resource=resource)
            if not check_resource_status.exists():
                ResourceStatus(resource=resource, 
                waiting_for_tagging=True, 
                status_description='Waiting for tagging').save()   

        if "_approve" in request.POST:
            resource = Resource.objects.get(id=obj.pk)
            
            check_tagging_resource = TaggingResource.objects.filter(resource=resource)
            if not check_tagging_resource.exists():
                TaggingResource(resource=resource).save()
                            
            check_resource_status = ResourceStatus.objects.filter(resource=resource)
            if not check_resource_status.exists():
                ResourceStatus(resource=resource, 
                waiting_for_tagging=True, 
                status_description='Waiting for tagging').save()
            else:
                resource_status = ResourceStatus.objects.get(resource=resource)   
                resource_status.waiting_for_tagging = False
                resource_status.is_tagged = True
                resource_status.waiting_for_approval = False
                resource_status.is_approved = True
                resource_status.status_description = 'Approved.'
                resource_status.save()
        return super().response_change(request, obj)


    def current_status(self, obj):
        check_resource_status = ResourceStatus.objects.filter(resource=obj)
        if check_resource_status.exists():
            resource_status = ResourceStatus.objects.get(resource=obj)
            return resource_status.status_description
        else:
            return 'Creating the resource'


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
                if model_obj.added_by == request.user or request.user.groups.name == 'Project coordinators':
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
                if model_obj.added_by == request.user or request.user.groups.name == 'Project coordinators':
                    return True
                else:
                    return False
            else:
                return False
        return False

    
    def save_model(self, request, obj, form, change):
        if obj.added_by is None or obj.added_by == '':
            obj.added_by = request.user
        super().save_model(request, obj, form, change)
        resource = Resource.objects.get(id=obj.pk)
        check_tagging_resource = TaggingResource.objects.filter(resource=resource)
        if not check_tagging_resource.exists():
            TaggingResource(resource=resource).save()
        check_resource_status = ResourceStatus.objects.filter(resource=resource)
        if not check_resource_status.exists():
            ResourceStatus(resource=resource, 
            waiting_for_tagging=True, 
            status_description='Waiting for tagging').save()   
    
