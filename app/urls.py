from django.urls import path, re_path
from app.views import *

urlpatterns = (
    path('categories', get_categories),
    path('search-options', get_search_options),
    path('search', search_api),
    path('resource', get_resource)
)
