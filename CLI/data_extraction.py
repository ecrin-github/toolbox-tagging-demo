import os
import sys

import csv
import json


if __name__ == '__main__':
    # Setup environ
    sys.path.append(os.getcwd())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toolbox.settings")

    import django
    django.setup()

    from resources.models import *
    from tagging.models import *


    def save_to_json():

        resources = []

        all_resources = Resource.objects.all()

        for res in all_resources:
            assigned_tags_check = TaggingResource.objects.filter(resource=res)
            if assigned_tags_check.exists():
                assigned_tags = TaggingResource.objects.filter(resource=res).first()

                sensitive_data_string = ''
                sensitive_data = assigned_tags.sensitive_data.all()
                if sensitive_data is not None:
                    for sen_data in sensitive_data:
                        sensitive_data_string += sen_data.name + '; '
                else:
                    resource_types_string = 'NaN'

                resource_types_string = ''
                resource_types = assigned_tags.resource_type.all()
                if resource_types is not None:
                    for res_type in resource_types:
                        resource_types_string += res_type.name + '; '
                else:
                    resource_types_string = 'NaN'

                research_field_string = ''
                research_field = assigned_tags.research_field.all()
                if research_field is not None:
                    for res_field in research_field:
                        research_field_string += res_field.name + '; '
                else:
                    research_field_string = 'NaN'

                geographical_scope_string = ''
                geographical_scope = assigned_tags.geographical_scope
                if geographical_scope is not None:
                    geographical_scope_string = geographical_scope.name
                else:
                    geographical_scope_string = 'NaN'

                countries_grouping_string = ''
                countries_grouping = assigned_tags.countries_grouping.all()
                if countries_grouping is not None:
                    for country in countries_grouping:
                        countries_grouping_string += country.name + '; '

                specific_topics_string = ''
                specific_topics = assigned_tags.specific_topics.all()
                if specific_topics is not None:
                    for spec_topic in specific_topics:
                        specific_topics_string += spec_topic.name + '; '
                else:
                    specific_topics_string = 'NaN'

                data_type_string = ''
                data_type = assigned_tags.data_type
                if data_type is not None:
                    data_type_string = data_type.name
                else:
                    data_type_string = 'NaN'

                data_type_subs_string = ''
                data_type_subs = assigned_tags.data_type_subs.all()
                if data_type_subs is not None:
                    for d_t_s in data_type_subs:
                        data_type_subs_string += d_t_s.name + '; '

                stage_in_ds_string = ''
                stage_in_ds = assigned_tags.stage_in_ds
                if stage_in_ds is not None:
                    stage_in_ds_string = stage_in_ds.name
                else:
                    stage_in_ds_string = 'NaN'

                resources.append({
                    "id": res.id - 1,
                    "title": res.title,
                    "year_of_publication": res.year_of_publication,
                    "authors": res.authors,
                    "added_by": res.added_by.username,
                    "sensitive_data": sensitive_data_string,
                    "resource_type": resource_types_string,
                    "research_field": research_field_string,
                    "geographical_scope": geographical_scope_string,
                    "countries": countries_grouping_string,
                    "specific_topics": specific_topics_string,
                    "data_type": data_type_string,
                    "data_type_subs": data_type_subs_string,
                    "stage_in_ds": stage_in_ds_string
                })

        with open('data.json', 'w') as fp:
            json.dump(resources, fp)


    def write_to_csv():

        with open('data.json', 'r') as fr:
            data = json.load(fr)

        with open('data.csv', 'w') as fp:
            fields = [
                "id",
                "title",
                "year_of_publication",
                "authors",
                "added_by",
                "sensitive_data",
                "resource_type",
                "research_field",
                "geographical_scope",
                "countries",
                "specific_topics",
                "data_type",
                "data_type_subs",
                "stage_in_ds"
            ]

            writer = csv.DictWriter(fp, fields)

            writer.writeheader()
            for row in data:
                writer.writerow(row)


    save_to_json()
    write_to_csv()


