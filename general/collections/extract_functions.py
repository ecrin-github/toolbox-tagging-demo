import json


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
        return int(year)
    else:
        return 0
