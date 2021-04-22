from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from categories.models import *


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):
    
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
        perms = request.user.groups.permissions.filter(codename='access_to_categories')
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
        perms = request.user.groups.permissions.filter(codename='access_to_categories')
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
        perms = request.user.groups.permissions.filter(codename='access_to_categories')
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


@admin.register(CountryGrouping)
class CountryGroupingAdmin(admin.ModelAdmin):
    
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
        perms = request.user.groups.permissions.filter(codename='access_to_categories')
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
        perms = request.user.groups.permissions.filter(codename='access_to_categories')
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


@admin.register(DataTypeSub)
class DataTypeSubAdmin(admin.ModelAdmin):
    
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
        perms = request.user.groups.permissions.filter(codename='access_to_categories')
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
        perms = request.user.groups.permissions.filter(codename='access_to_categories')
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
        perms = request.user.groups.permissions.filter(codename='access_to_categories')
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
