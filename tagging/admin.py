from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


csrf_protected_method = method_decorator(csrf_protect)


# Register your models here.
