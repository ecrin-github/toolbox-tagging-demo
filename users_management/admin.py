from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from django.contrib.auth.models import Group
from users_management.models import ContentManager, TaggingUser, ProjectCoordinator


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
# Project coordinators admin model
@admin.register(ProjectCoordinator)
class ProjectCoordinatorAdmin(admin.ModelAdmin):
    exclude = [
        'user_permissions', 
        'is_staff', 
        'is_superuser', 
        'last_login', 
        'date_joined',
        'is_active',
        'groups',
    ]

    fields = ('username', 'password', 'first_name', 'last_name', 'email',)

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
        group = Group.objects.get(name='Project coordinators')
        if obj.pk:
            orig_obj = ProjectCoordinator.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.is_staff = True
        obj.is_active = True
        obj.is_superuser = True
        obj.save()

        user = ProjectCoordinator.objects.get(id=obj.pk)
        
        users_in_group = group.user_set.all()
        
        if not users_in_group.filter(id=user.groups_id).exists():
            group.user_set.add(user)


# Content managers admin model
@admin.register(ContentManager)
class ContentManagerAdmin(admin.ModelAdmin):
    exclude = [
        'user_permissions', 
        'is_staff', 
        'is_superuser', 
        'last_login', 
        'date_joined',
        'is_active',
        'groups',
    ]

    fields = ('username', 'password', 'first_name', 'last_name', 'email',)

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
        group = Group.objects.get(name='Content managers')
        if obj.pk:
            orig_obj = ContentManager.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.is_staff = True
        obj.is_active = True
        obj.is_superuser = True
        obj.save()

        user = ContentManager.objects.get(id=obj.pk)
        
        users_in_group = group.user_set.all()
        
        if not users_in_group.filter(id=user.groups_id).exists():
            group.user_set.add(user)


# Tagging users admin model
@admin.register(TaggingUser)
class TaggingUserAdmin(admin.ModelAdmin):
    exclude = [
        'user_permissions', 
        'is_staff', 
        'is_superuser', 
        'last_login', 
        'date_joined',
        'is_active',
        'groups',
    ]

    fields = ('username', 'password', 'first_name', 'last_name', 'email',)

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
        group = Group.objects.get(name='Tagging group')
        if obj.pk:
            orig_obj = TaggingUser.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.is_staff = True
        obj.is_active = True
        obj.is_superuser = True
        obj.save()
        
        user = TaggingUser.objects.get(id=obj.pk)
        
        users_in_group = group.user_set.all()
        
        if not users_in_group.filter(id=user.groups_id).exists():
            group.user_set.add(user)
