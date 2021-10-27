from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from categories.models import *


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
@admin.register(SensitiveData)
class SensitiveDataAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = SensitiveData.objects.all().order_by('id')
        return qs

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_categories')
            if perms.exists():
                return True
            return False
        except:
            pass


@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = ResourceType.objects.all().order_by('id')
        return qs

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_categories')
            if perms.exists():
                return True
            return False
        except:
            pass


@admin.register(ResearchField)
class ResearchFieldAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = ResearchField.objects.all().order_by('id')
        return qs

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_categories')
            if perms.exists():
                return True
            return False
        except:
            pass


class CountryGroupingInline(admin.TabularInline):
    model = CountryGrouping


@admin.register(GeographicalScope)
class GeographicalScopeAdmin(admin.ModelAdmin):
    inlines = [
        CountryGroupingInline
    ]

    def get_queryset(self, request):
        qs = GeographicalScope.objects.all().order_by('id')
        return qs

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_categories')
            if perms.exists():
                return True
            return False
        except:
            pass


class DataTypeSubInline(admin.TabularInline):
    model = DataTypeSub


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    inlines = [
        DataTypeSubInline
    ]

    def get_queryset(self, request):
        qs = DataType.objects.all().order_by('id')
        return qs

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_categories')
            if perms.exists():
                return True
            return False
        except:
            pass


@admin.register(SpecificTopic)
class SpecificTopicAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = SpecificTopic.objects.all().order_by('id')
        return qs

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_categories')
            if perms.exists():
                return True
            return False
        except:
            pass


@admin.register(StageInDS)
class StageInDSAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = StageInDS.objects.all().order_by('id')
        return qs

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_categories')
        if perms.exists():
            return True
        return False

    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_categories')
            if perms.exists():
                return True
            return False
        except:
            pass
