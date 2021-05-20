from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from django.utils.safestring import mark_safe

from categories.models import SpecificTopic
from tagging.models import TaggingResource
from resources.models import ResourceStatus, Resource
from general.configs import HOST


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
@admin.register(TaggingResource)
class TaggingResourceAdmin(admin.ModelAdmin):

    change_form_template = 'tagging/change_tagging.html'

    fieldsets = (
        ('Bibliographic data', {
            "fields": (
                'resource',
                'short_title',
                'abstract',
                'authors',
                'year_of_publication',
                'doi',
                'language',
                'type_of_resource',
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
        'short_title',
        'abstract',
        'authors',
        'year_of_publication',
        'doi',
        'language',
        'type_of_resource',
        'url',
        'attached_file',
        'created',
        'updated',
        'added_by',
        'current_status',
    )


    def get_queryset(self, request):
        if request.user.groups.name == 'Project coordinators' or request.user.groups.name == 'Content managers':
            qs = TaggingResource.objects.all()
        else:
            qs = TaggingResource.objects.filter(resource__tagging_persons__id=request.user.id)
        return qs


    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['is_disabled'] = True
        extra_context['is_tagger'] = True
        return super().add_view(request, form_url=form_url, extra_context=extra_context)


    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        tagging_resource = TaggingResource.objects.get(id=object_id)
        resource = Resource.objects.get(id=tagging_resource.resource.id)
        resource_status = ResourceStatus.objects.get(resource__id=resource.id)
        if resource_status.waiting_for_tagging:
            extra_context['is_disabled'] = False
        else:
            extra_context['is_disabled'] = True
        check_tagger = Resource.objects.filter(id=tagging_resource.resource.id, tagging_persons__id=request.user.id)
        if check_tagger.exists():
            extra_context['is_tagger'] = True
        else:
            extra_context['is_tagger'] = False
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)


    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': False,
            'show_save_and_add_another': False
        })
        if request.user.groups.name == 'Project coordinator' or request.user.groups.name == 'Tagging group':
            context['adminform'].form.fields['specific_topics'].queryset = SpecificTopic.objects.all().order_by('id')
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)


    def response_change(self, request, obj):
        if "_save-and-continue-tagging" in request.POST:
            obj.save()
        
        if "_approve" in request.POST:
            obj.save()
            resource_status = ResourceStatus.objects.get(resource__id=obj.resource.id)
            resource_status.waiting_for_tagging = False
            resource_status.is_tagged = True
            resource_status.waiting_for_approval = True
            resource_status.is_approved = False
            resource_status.status_description = 'Tagged. Waiting for approval.'
            resource_status.save()

        return super().response_change(request, obj)


    def short_title(self, obj):
        if obj.resource.short_title is not None and obj.resource.short_title != '':
            return obj.resource.short_title
        return 'None'


    def authors(self, obj):
        if obj.resource.authors is not None and obj.resource.authors != '':
            return obj.resource.authors
        return 'None'


    def abstract(self, obj):
        if obj.resource.abstract is not None and obj.resource.abstract != '':
            return obj.resource.abstract
        return 'None'


    def year_of_publication(self, obj):
        if obj.resource.year_of_publication is not None and obj.resource.year_of_publication != '':
            return obj.resource.year_of_publication
        return 'None'


    def doi(self, obj):
        if obj.resource.doi is not None and obj.resource.doi != '':
            return obj.resource.doi
        return 'None'


    def language(self, obj):
        if obj.resource.language.name is not None and obj.resource.language.name != '':
            return obj.resource.language.name
        return 'None'


    def type_of_resource(self, obj):
        if obj.resource.type_of_resource.name is not None and obj.resource.type_of_resource.name != '':
            return obj.resource.type_of_resource.name
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

    
    def current_status(self, obj):
        check_resource_status = ResourceStatus.objects.filter(resource__id=obj.resource.id)
        if check_resource_status.exists():
            resource_status = ResourceStatus.objects.get(resource__id=obj.resource.id)
            return resource_status.status_description
        else:
            return 'Unknown status'


    def created(self, obj):
        if obj.resource.created is not None and obj.resource.created != '':
            return obj.resource.created
        return 'None'


    def updated(self, obj):
        if obj.resource.updated is not None and obj.resource.updated != '':
            return obj.resource.updated
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
        if obj:
            perms = request.user.groups.permissions.filter(codename='assign_categories')
            tagging_resource = TaggingResource.objects.get(id=obj.id)
            user_check = Resource.objects.filter(id=tagging_resource.resource.id, tagging_persons__id=request.user.id)
            status_check = ResourceStatus.objects.get(resource__id=obj.resource.id)
            if (perms.exists() and user_check.exists() and status_check.is_tagged == False and status_check.waiting_for_tagging == True) or (request.user.groups.name == 'Project coordinators'):
                return True
        else:
            return False

    
    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    
    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        if request.user.groups.name == 'Project coordinators':
            return True
        return False

    
    @csrf_protected_method
    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)
