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

# print(os.getcwd())

def bazaar_craft_flips():
    for key, value in BAZAAR_API['products'].items():
        current_item = item_array[index_of_item_in_item_arr[key]]
        current_item.latest_bazaar_data = value
bazaar_craft_flips()

print(item_array[index_of_item_in_item_arr['ENCHANTED_DIAMOND']].latest_bazaar_data)
def update_bazaar_value():
    for key, value in BAZAAR_API['products']:
        current_item = item_array[index_of_item_in_item_arr[key]]
        current_item.latest_bazaar_data = value

"""

There seem to be lots of stuff about daily volume of an item in general,
the system idea currently in place seems to be wayy too vague, maybe it should be somethign that runs 24/7
like for now we want to make a simple function that returns the items with the hugest gaps in making them and 
getting them sold.
after we figure that out maybe we can work on a mod solution that tries to do other things.

for now I'll just build something that outputs the best craft flips (WITH TAXES CALCULATED).
"""
