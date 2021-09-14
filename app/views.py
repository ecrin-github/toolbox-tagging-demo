import json

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from tagging.models import *
from resources.models import TypeOfResource
from django.core.paginator import Paginator


def tags_mapper(res_id: int):
    if res_id is not None:

        tags = TaggingResource.objects.filter(resource__id=res_id)

        if tags.exists():
            tags = TaggingResource.objects.get(resource__id=res_id)

            resource_types = []
            if tags.resource_type is not None:
                for rt in tags.resource_type.all():
                    rt_record = {
                        'name': rt.name,
                        'description': rt.description
                    }
                    resource_types.append(rt_record)

            research_fields = []
            if tags.research_field is not None:
                for rf in tags.research_field.all():
                    rf_record = {
                        'name': rf.name,
                        'description': rf.description
                    }
                    research_fields.append(rf_record)

            specific_topics = []
            if tags.specific_topics is not None:
                for st in tags.specific_topics.all():
                    st_record = {
                        'name': st.name,
                        'description': st.description
                    }
                    specific_topics.append(st_record)

            data_type_subs = []
            if tags.data_type_subs is not None:
                for data_sub in tags.data_type_subs.all():
                    data_sub_record = {
                        'name': data_sub.name,
                        'description': data_sub.name
                    }
                    data_type_subs.append(data_sub_record)

            countries_grouping = []
            if tags.countries_grouping is not None:
                for country in tags.countries_grouping.all():
                    countries_grouping.append(country.name)

            return {
                'resource_type': resource_types,
                'research_field': research_fields,
                'specific_topics': specific_topics,
                'geographical_scope': {
                    'name': tags.geographical_scope.name if tags.geographical_scope is not None else None,
                    'description': tags.geographical_scope.description if tags.geographical_scope is not None else None,
                    'countries_grouping': countries_grouping
                },
                'data_type': {
                    'name': tags.data_type.name if tags.data_type is not None else None,
                    'description': tags.data_type.description if tags.data_type is not None else None,
                    'subs': data_type_subs
                },
                'stage_in_ds': {
                    'name': tags.stage_in_ds.name if tags.stage_in_ds is not None else None,
                    'description': tags.stage_in_ds.description if tags.stage_in_ds is not None else None
                },
            }
        else:
            return None
    else:
        return None


def resource_mapper(resource_id: int):

    resource_filter = Resource.objects.filter(id=resource_id)

    if resource_filter.exists():
        resource = Resource.objects.get(id=resource_id)

        resource_file_url = None
        if resource.resource_file and hasattr(resource.resource_file, 'url'):
            resource_file_url = resource.resource_file.url

        return {
            'id': resource.id,
            'title': resource.title,
            'abstract': resource.abstract,
            'authors': resource.authors,
            'year_of_publication': resource.year_of_publication,
            'doi': resource.doi,
            'language': resource.language.name if resource.language is not None else None,
            'type_of_resource': resource.type_of_resource.name if resource.type_of_resource is not None else None,
            'url': resource.url,
            'resource_file': resource_file_url,
            'tags': tags_mapper(resource.id),
            'created': resource.created,
            'updated': resource.updated,
        }
    else:
        return None


# Create your views here.
def get_categories(request):
    all_resource_types = ResourceType.objects.all()
    all_research_fields = ResearchField.objects.all()
    all_specific_topics = SpecificTopic.objects.all()
    all_geo_scope = GeographicalScope.objects.all()
    all_data_types = DataType.objects.all()
    all_stages_in_ds = StageInDS.objects.all()
    all_types_of_resource = TypeOfResource.objects.all()

    resource_types_filters = []
    for rtf in all_resource_types:
        rtf_record = {
            'id': rtf.id,
            'modelPropertyName': 'id',
            'resourcePropertyName': 'resource_type',
            'name': rtf.name,
            'isSelected': False
        }
        resource_types_filters.append(rtf_record)

    research_fields_filters = []
    for rff in all_research_fields:
        rff_record = {
            'id': rff.id,
            'modelPropertyName': 'id',
            'resourcePropertyName': 'research_field',
            'name': rff.name,
            'isSelected': False
        }
        research_fields_filters.append(rff_record)

    specific_topics_filters = []
    for stf in all_specific_topics:
        stf_record = {
            'id': stf.id,
            'modelPropertyName': 'id',
            'resourcePropertyName': 'specific_topics',
            'name': stf.name,
            'isSelected': False
        }
        specific_topics_filters.append(stf_record)

    stage_in_ds_filters = []
    for sdf in all_stages_in_ds:
        sdf_record = {
            'id': sdf.id,
            'modelPropertyName': 'id',
            'resourcePropertyName': 'stage_in_ds',
            'name': sdf.name,
            'isSelected': False
        }
        stage_in_ds_filters.append(sdf_record)

    type_of_resource_filters = []
    for tor in all_types_of_resource:
        tor_record = {
            'id': tor.id,
            'modelPropertyName': 'id',
            'resourcePropertyName': 'type_of_resource',
            'name': tor.name,
            'isSelected': False
        }
        type_of_resource_filters.append(tor_record)

    geo_scope_filters = []
    for gsf in all_geo_scope:

        countries_filters = []
        all_countries = CountryGrouping.objects.filter(geographical_scope=gsf)
        if all_countries.exists():
            for country in all_countries:
                country_record = {
                    'id': country.id,
                    'modelPropertyName': 'id',
                    'resourcePropertyName': 'countries_grouping',
                    'name': country.name,
                    'isSelected': False
                }
                countries_filters.append(country_record)

        gsf_record = {
            'id': gsf.id,
            'modelPropertyName': 'id',
            'resourcePropertyName': 'geographical_scope',
            'name': gsf.name,
            'isSelected': False,
            'children': countries_filters
        }
        geo_scope_filters.append(gsf_record)

    data_types_filters = []
    for dtf in all_data_types:

        data_subtypes_filters = []
        all_data_subtypes = DataTypeSub.objects.filter(data_type=dtf)

        if all_data_subtypes.exists():
            for data_sub in all_data_subtypes:
                data_sub_record = {
                    'id': data_sub.id,
                    'modelPropertyName': 'id',
                    'resourcePropertyName': 'data_type_subs',
                    'name': data_sub.name,
                    'isSelected': False
                }
                data_subtypes_filters.append(data_sub_record)

        dtf_record = {
            'id': dtf.id,
            'modelPropertyName': 'id',
            'resourcePropertyName': 'data_type',
            'name': dtf.name,
            'isSelected': False,
            'children': data_subtypes_filters
        }
        data_types_filters.append(dtf_record)

    categories = [
        {
            'id': 1,
            'isSelected': False,
            'appName': 'resources',
            'modelName': 'TypeOfResource',
            'name': 'Item type',
            'hasChildren': False,
            'filters': type_of_resource_filters
        },
        {
            'id': 2,
            'isSelected': False,
            'appName': 'tagging',
            'modelName': 'ResourceType',
            'name': 'Resource types',
            'hasChildren': False,
            'filters': resource_types_filters
        },
        {
            'id': 3,
            'isSelected': False,
            'appName': 'tagging',
            'modelName': 'ResearchField',
            'name': 'Research fields',
            'hasChildren': False,
            'filters': research_fields_filters
        },
        {
            'id': 4,
            'isSelected': False,
            'appName': 'tagging',
            'modelName': 'SpecificTopic',
            'name': 'Specific topics',
            'hasChildren': False,
            'filters': specific_topics_filters
        },
        {
            'id': 5,
            'isSelected': False,
            'appName': 'tagging',
            'modelName': 'GeographicalScope',
            'name': 'Geographical scope',
            'hasChildren': True,
            'filters': geo_scope_filters
        },
        {
            'id': 6,
            'isSelected': False,
            'appName': 'tagging',
            'modelName': 'DataType',
            'name': 'Data types',
            'hasChildren': True,
            'filters': data_types_filters
        },
        {
            'id': 7,
            'isSelected': False,
            'appName': 'tagging',
            'modelName': 'StageInDs',
            'hasChildren': False,
            'name': 'Stage in data sharing',
            'filters': stage_in_ds_filters
        },
    ]

    return JsonResponse(categories, safe=False)


def get_search_options(request):
    search_options = [
        {
            'id': 1,
            'name': 'Title',
            'appName': 'resources',
            'modelName': 'Resource',
            'propertyName': 'resource__title',
            'isDefault': True
        },
        {
            'id': 2,
            'name': 'DOI',
            'appName': 'resources',
            'modelName': 'Resource',
            'propertyName': 'resource__doi',
            'isDefault': False
        },
        {
            'id': 3,
            'name': 'Author(s)',
            'appName': 'resources',
            'modelName': 'Resource',
            'propertyName': 'resource__authors',
            'isDefault': False
        }
    ]

    return JsonResponse(search_options, safe=False)


@csrf_exempt
def search_api(request):
    if request.method == 'POST':
        request_body_json = json.loads(request.body)

        if request_body_json['searchType']['propertyName'] == 'resource__doi':
            query_lookup = '{0}__contains'.format(request_body_json['searchType']['propertyName'])
            query_value = request_body_json['searchValue']

            query = Q(**{query_lookup: query_value})

            filters = request_body_json['filters']
        else:
            query = Q()

            query_lookup = '{0}__contains'.format(request_body_json['searchType']['propertyName'])
            query_value = request_body_json['searchValue']

            query.add(Q(**{query_lookup: query_value}), Q.OR)

            query_value_split = query_value.split(" ")

            for word in query_value_split:
                query.add(Q(**{query_lookup: word}), Q.OR)

            filters = request_body_json['filters']

        page = None
        if 'page' in request_body_json:
            try:
                page = int(request_body_json['page'])
            except:
                page = None

        size = None
        if 'size' in request_body_json:
            try:
                size = int(request_body_json['size'])
            except:
                size = None

        filters_to_apply = {}
        for key in filters:
            if isinstance(filters[key], list) and len(filters[key]) > 0:
                filters_to_apply[key] = filters[key]
            else:
                if not isinstance(filters[key], list):
                    if filters[key] > 0:
                        filters_to_apply[key] = filters[key]

        get_resources = TaggingResource.objects\
            .filter(query)\
            .filter(**filters_to_apply)\
            .order_by('id')

        if get_resources.exists():

            data = []

            if page is not None and size is not None:
                paginator = Paginator(get_resources, size)
                objects = paginator.get_page(page)

                for resource in objects:
                    data.append(resource_mapper(resource.resource_id))

                response = {
                    'total': get_resources.count(),
                    'data': data
                }

            else:
                for resource in get_resources:
                    data.append(resource_mapper(resource.resource_id))

                response = {
                    'total': get_resources.count(),
                    'data': data
                }
        else:
            response = {
                'total': 0,
                'data': []
            }
        return JsonResponse(response, safe=False)

    else:
        response = {
            'total': 0,
            'data': []
        }
        return JsonResponse(response, safe=False)


@csrf_exempt
def get_resource(request):
    if request.method == 'POST':
        request_body_json = json.loads(request.body)

        try:
            if request_body_json['id'] is not None:

                resource_id = int(request_body_json['id'])

                res_filter = Resource.objects.filter(id=resource_id)

                if res_filter.exists():

                    return JsonResponse(resource_mapper(resource_id), safe=False)

                else:
                    return JsonResponse({}, safe=False)

            else:
                return JsonResponse({}, safe=False)

        except:
            return JsonResponse({}, safe=False)
