import json
from pyzotero import zotero


def read_file(filename: str):
        with open(filename, 'r') as fp:
            data = json.load(fp)
        return data


def convert_authors(authors_list: list) -> str:
    authors = ''
    if len(authors_list) > 0 and authors_list is not None:
        if len(authors_list) > 1:
            for author_data in authors_list:
                author_string = ''
                if 'firstName' in author_data:
                    author_string += author_data['firstName'] + ' '
                if 'lastName' in author_data:
                    author_string += author_data['lastName'] + ''
                if 'name' in author_data:
                    author_string += author_data['name'] + ''
                
                authors += author_string + '; '
        elif len(authors_list) == 1:
            author_string = ''
            if 'firstName' in authors_list[0]:
                author_string += authors_list[0]['firstName'] + ' '
            if 'lastName' in authors_list[0]:
                author_string += authors_list[0]['lastName'] + ''
            if 'name' in authors_list[0]:
                author_string += authors_list[0]['name'] + ''
            
            authors = author_string
        
    return authors


def convert_year(year: str) -> int:
    if year != '' and year is not None:
        try:
            return int(year)
        except:
            return 0
    else:
        return 0


def save_collection_to_file(privateKey: str, userID: str, libraryType: str, collectionID: str, filename: str):
    zot = zotero.Zotero(library_id=userID, library_type=libraryType, api_key=privateKey)

    collection_items = zot.collection_items(collectionID)

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