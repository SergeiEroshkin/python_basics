import sys
import requests
import json

"""suitcase_url = str(sys.argv[1])
#'http://pkit.wopr.c2x.io:8000/suitcases/rolly'
inventory_url = str(sys.argv[2])
#'http://pkit.wopr.c2x.io:8000/robots/hey-you/parts'"""


def get_suitcase_size():
    suitecase_size = requests.get('http://pkit.wopr.c2x.io:8000/suitcases/rolly')
    return suitecase_size.json()['volume']


def get_most_valuable_items():
    inventory = requests.get('http://pkit.wopr.c2x.io:8000/robots/hey-you/parts').json()
    suitcase_volume = get_suitcase_size()
    new_dict ={}
    id_list = []
    total = 0
    for part in range(len(inventory)):
        max_value = max(inventory, key=lambda x: x['value'])
        suitcase_volume -= max_value["volume"]
        id_list.append(str(max_value["id"]))
        inventory.remove(max_value)
        total += max_value["volume"]
        if suitcase_volume <= 0:
            break
    new_dict["part_ids"] = sorted(id_list)
    new_dict["value"] = total
    return json.dumps(new_dict)

print get_most_valuable_items()