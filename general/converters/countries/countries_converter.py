import json


MODEL_NAME = 'categories.CountryGrouping'
PK_START_WITH = 15
GROUP_ID = 5


def converter():
    with open('countries.json', 'r') as json_data:
        data = json.load(json_data)
    
    objs = []
    pk = PK_START_WITH

    for country in data:
        obj = {
            "model": MODEL_NAME,
            "pk": pk,
            "fields": {
                "name": country['name'],
                "geographical_scope_id": GROUP_ID
            }
        }
        objs.append(obj)
        pk += 1

    with open('countries_converted.json', 'w') as outfile:
        json.dump(objs, outfile)

    print('FINISHED!')


converter() 
