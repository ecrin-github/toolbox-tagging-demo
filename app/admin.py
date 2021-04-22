from django.contrib import admin
import csv
from django.http import HttpResponse
import datetime
from itertools import chain


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field for field in meta.fields]
        many_to_many_field_names = set([many_to_many_field for many_to_many_field in meta.many_to_many if many_to_many_field.name != 'tagging_persons'])
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        fields_names_header = [str(field.verbose_name).capitalize() for field in field_names]
        many_to_many_field_names_header = [str(many_to_many_field.verbose_name).capitalize() for many_to_many_field in many_to_many_field_names]

        writer.writerow(list(chain(fields_names_header, many_to_many_field_names_header)))
        for obj in queryset:
            row = []
            for field in field_names:
                value = getattr(obj, field.name)
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                row.append(value)
            for field in many_to_many_field_names:
                values = getattr(obj, field.name).all().values_list('name', flat=True)
                result_string = ""
                if values:
                    if len(values) > 1:
                        for val in values:
                            result_string += val + "; "
                        row.append(result_string)
                    elif len(values) == 1:
                        result_string = values[0]                        
                        row.append(result_string)
                else:
                    row.append(result_string)
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Export Selected"


# Register your models here.
