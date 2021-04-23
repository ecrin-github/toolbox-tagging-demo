from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from users_management.models import *


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = [
        'user_permissions', 
        'is_staff', 
        'is_superuser', 
        'last_login', 
        'date_joined',
        'is_active'
    ]

    fields = ('username', 'password', 'first_name', 'last_name', 'email', 'groups',)

    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_users')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_users')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_users')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_users')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_users_and_groups')
            if perms.exists():
                return True
            return False
        except:
            pass
    

    def save_model(self, request, obj, form, change):
        if obj.pk:
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.is_staff = True
        obj.is_active = True
        obj.is_superuser = True
        obj.save()


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    
    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_users')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_users')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_users')
        if perms.exists():
            return True
        return False

    
    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_users')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_users_and_groups')
            if perms.exists():
                return True
            return False
        except:
            pass
