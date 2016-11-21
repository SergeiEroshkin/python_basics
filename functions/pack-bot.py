import sys
import requests
import json

suitcase_url = str(sys.argv[1])
#'http://pkit.wopr.c2x.io:8000/suitcases/rolly'
inventory_url = str(sys.argv[2])
#'http://pkit.wopr.c2x.io:8000/robots/hey-you/parts'


def get_suitcase_size():
    suitcase_size = requests.get('http://pkit.wopr.c2x.io:8000/suitcases/rolly')
    return suitcase_size.json()['volume']


def get_density_dict():
    inventory = requests.get('http://pkit.wopr.c2x.io:8000/robots/hey-you/parts').json()
    for part in inventory:
        item_density = ((float(part['value'])/float(part['volume'])))
        part['gross_value'] = item_density
    ccc = sorted(inventory, key=lambda gross_value: gross_value['gross_value'], reverse=True)
    return ccc


def get_most_valuable_set():
    suitcase_volume = get_suitcase_size()
    density_parts = get_density_dict()
    new_dict ={}
    id_list = []
    total = 0
    for part in density_parts:
        suitcase_volume -= part['volume']
        if suitcase_volume <= 0:
            break
        id_list.append(part['id'])
        total += part['volume']

    new_dict['part_ids'] = id_list
    new_dict['value'] = total
    return json.dumps(new_dict, sort_keys=True, indent=4, separators=(',', ':'))

print get_most_valuable_set()
