from Item_Utils import Item
import Item_Utils as Item_utils
import time
import requests
import os

BAZAAR_API = requests.get('https://api.hypixel.net/skyblock/bazaar').json()

item_array = Item_utils.return_item_array()
index_of_item_in_item_arr = {}

n = 0

for item in item_array:
    index_of_item_in_item_arr[item.internal_name] = n
    n += 1

print(os.getcwd())

def bazaar_craft_flips():
    for key, value in BAZAAR_API['products']:
        current_item = item_array[index_of_item_in_item_arr[key]]
        current_item.latest_bazaar_data = value