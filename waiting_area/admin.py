from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from waiting_area.models import WaitingResource
from resources.models import Resource


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
@admin.register(WaitingResource)
class WaitingResourceAdmin(admin.ModelAdmin):
    
    @csrf_protected_method
    def has_module_permission(self, request):
        try:
            perms = request.user.groups.permissions.filter(codename='access_to_waiting_area')
            if perms.exists():
                return True
            return False
        except:
            pass


    def get_queryset(self, request):        
        qs = super().get_queryset(request)
        return qs.filter(resource__tagging_persons=request.user)


    @csrf_protected_method
    def has_add_permission(self, request):
        perms = request.user.groups.permissions.filter(codename='add_waitings')
        if perms.exists() and request.user.groups.name != 'Tagging group':
            return True
        return False    


    @csrf_protected_method
    def has_view_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='view_waitings')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='edit_waitings')
        if perms.exists():
            return True
        return False


    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        perms = request.user.groups.permissions.filter(codename='remove_waitings')
        if perms.exists() and request.user.groups.name != 'Tagging group':
            return True
        return False


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
