import os
import sys


if __name__ == '__main__':
    # Setup environ
    dir_path = '/Users/iproger/Projects/ecrin-mdr/toolbox'
    # dir_path = '/var/www/toolbox'
    sys.path.append(dir_path)
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toolbox.settings")

    import django
    django.setup()


    from general.collections.zotero_configs import PRIVATE_KEY, USER_ID, LIBRARY_TYPE
    from general.collections.extract_functions import save_collection_to_file, \
        read_file, convert_authors, convert_year
    

    # GLOBAL VARIABLES
    COLLECTION_ID = '3FM8UU6H'
    FILENAME = '/Users/iproger/Projects/ecrin-mdr/toolbox/general/collections/ecrin/ecrin_data_collection.json'

    '''
    save_collection_to_file(
        privateKey=PRIVATE_KEY, 
        userID=USER_ID, 
        libraryType=LIBRARY_TYPE, 
        collectionID=COLLECTION_ID, 
        filename=FILENAME
    )
    '''

    from users_management.models import User
    from resources.models import Resource, ResourceStatus, Language, ResourceType
    from tagging.models import TaggingResource


    def collection_importer():
        data = read_file(FILENAME)
        for item in data:
            if item['language'] is not None and item['language'] != '':
                language = Language.objects.filter(code=item['language'])
                if language.exists():
                    lang = Language.objects.get(code=item['language'])
                else:
                    lang = None
            else:
                lang = None

            if item['type_of_resource'] is not None and item['type_of_resource'] != '':
                type_of_resource = ResourceType.objects.filter(name=item['type_of_resource'])
                if type_of_resource.exists():
                    res_type = ResourceType.objects.get(name=item['type_of_resource'])
                else:
                    res_type = None
            else:
                res_type = None

            content_manager = User.objects.get(username='ECRIN_CM')
            tagging_person = User.objects.get(username='ECRIN_Tagger')

            resource = Resource(
                title=item['title'] if 'title' != '' else 'None',
                short_title=item['shortTitle'],
                abstract=item['abstract'],
                authors=convert_authors(item['authors']),
                year_of_publication=convert_year(item['year']),
                doi=item['doi'],
                language=lang,
                type_of_resource=res_type,
                url=item['url'],
                resource_file=None,
                added_by=content_manager,
            )
            resource.save()
            res = Resource.objects.get(id=resource.id)
            res.tagging_persons.add(tagging_person.id)

            res_status = ResourceStatus(
                resource_id=resource.id,
                waiting_for_tagging=True,
                status_description='Waiting for tagging'
            )
            res_status.save()

            tagging_res = TaggingResource(
                resource_id=resource.id
            )
            tagging_res.save()

            print('Resource has been added!')
        
        print('DONE!')


    collection_importer()
