from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from tagging.models import *


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    
    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_tags')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_tags')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_tags')
        if perms.exists():
            return True
        return False

    
    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='access_to_tags')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_tags')
            if perms.exists():
                return True
            return False
        except:
            pass
