import json


MODEL_NAME = 'resources.Language'
PK_START_WITH = 1


def converter():
    with open('languages_list.json', 'r') as json_data:
        data = json.load(json_data)
    
    objs = []
    pk = PK_START_WITH

    for lang in data:
        obj = {
            "model": MODEL_NAME,
            "pk": pk,
            "fields": {
                "name": lang['name'],
                "code": lang['code']
            }
        }
        objs.append(obj)
        pk += 1

    with open('languages_converted.json', 'w') as outfile:
        json.dump(objs, outfile)

    print('FINISHED!')


converter() 
