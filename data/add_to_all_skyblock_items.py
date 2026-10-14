import requests
import json

ITEM_API = requests.get('https://api.hypixel.net/resources/skyblock/items').json()

list_of_all_items = []
dict_of_all_items = {}

for i in ITEM_API['items']:
    dict_of_all_items[i['name']] = i['id']

with open('all_name_vs_id', 'w')as f:
    json.dump(dict_of_all_items, f, indent=2)