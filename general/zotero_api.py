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


    import json
    from pyzotero import zotero


    # GLOBAL VARIABLES
    PRIVATE_KEY = 'sDmtsYFa6c1PNW5kNqPWJ1Pd'
    USER_ID = '7003583'
    LIBRARY_TYPE = 'user'
    COLLECTION_ID = '3FM8UU6H'
    FILENAME = 'zotero_data.json'


    def save_collection_to_file(privateKey: str, userID: str, libraryType: str, collectionID: str, filename: str):
        zot = zotero.Zotero(library_id=userID, library_type=libraryType, api_key=privateKey)

        collection_items = zot.collection_items(COLLECTION_ID)

        final_items = []

        for item in collection_items:
            item_data = item['data']
            final_items.append({
                'title': item_data['title'] if 'title' in item_data else 'None',
                'shortTitle': item_data['shortTitle'] if 'shortTitle' in item_data else None,
                'abstract': item_data['abstractNote'] if 'abstractNote' in item_data else None,
                'authors': item_data['creators'] if 'creators' in item_data else None,
                'year': item_data['date'] if 'date' in item_data else None,
                'doi': item_data['DOI'] if 'DOI' in item_data else None,
                'language': item_data['language'] if 'language' in item_data else None,
                'type_of_resource': item_data['itemType'] if 'itemType' in item_data else None,
                'url': item_data['url'] if 'url' in item_data else None,
                'file': ''
            })
        
        with open(filename, 'w') as fp:
            json.dump(final_items, fp)

        print('DONE!')


    '''
    save_collection_to_file(
        privateKey=PRIVATE_KEY, 
        userID=USER_ID, 
        libraryType=LIBRARY_TYPE, 
        collectionID=COLLECTION_ID, 
        filename=FILENAME
    )
    '''


    def read_file(filename: str):
        with open(filename, 'r') as fp:
            data = json.load(fp)
        return data


    def convert_authors(authors_list: list) -> str:
        authors = ''
        if len(authors_list) > 0 and authors_list is not None:
            for author_data in authors_list:
                author_string = ''
                if 'firstName' in author_data:
                    author_string += author_data['firstName'] + ' '
                if 'lastName' in author_data:
                    author_string += author_data['lastName'] + ' '
                if 'name' in author_data:
                    author_string += author_data['name'] + ' '
                
                authors += author_string + '; '
        return authors

    
    def convert_year(year: str) -> int:
        if year != '' and year is not None:
            return int(year)
        else:
            return 0
    

    from users_management.models import User
    from resources.models import Resource, ResourceStatus, Language, ResourceType
    from tagging.models import TaggingResource


    def collection_importer():
        data = read_file(FILENAME)
        for item in data:
            if item['language'] is not None and item['language'] != '':
                language = Language.objects.filter(code=item['language'])
                if language.exists():
                    lang = Language.objects.filter(code=item['language']).first()
                else:
                    lang = None
            else:
                lang = None

            if item['type_of_resource'] is not None and item['type_of_resource'] != '':
                type_of_resource = ResourceType.objects.filter(name=item['type_of_resource'])
                if type_of_resource.exists():
                    res_type = ResourceType.objects.filter(name=item['type_of_resource']).first()
                else:
                    res_type = None
            else:
                res_type = None

            user = User.objects.get(username='content_manager_1')
            tagging_person = User.objects.get(username='tagging_user_1')

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
                added_by=user,
            )
            # resource.tagging_persons.set(tagging_person)
            resource.save()

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
    

    

    
