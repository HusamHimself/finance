import requests
import json

ITEM_API = requests.get('https://api.hypixel.net/resources/skyblock/items').json()

list_of_all_items = []
dict_of_all_items = {}

for i in ITEM_API['items']:
    list_of_all_items.append(i['id'])

dict_of_all_items['internal_name'] = list_of_all_items

with open('all_items.json', 'w')as f:
    json.dump(dict_of_all_items, f, indent=2)