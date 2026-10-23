import Item_Utils
import Order_Utils
import time
import requests
import os

BAZAAR_API = requests.get('https://api.hypixel.net/skyblock/bazaar').json()

item_array = Item_Utils.return_item_array()
index_of_item_in_item_arr = {}

n = 0

for item in item_array:
    index_of_item_in_item_arr[item.internal_name] = n
    n += 1

# print(os.getcwd())

def return_bazaar_array()-> list:
    final = []
    for item in item_array:
        if item.commerce_type == 'bazaar'and item.craft_parameters != {}:
            final.append(item)
    return final

def update_bazaar_data():
    for key, value in BAZAAR_API['products'].items():
        current_item = item_array[index_of_item_in_item_arr[key]]
        current_item.buy_summary = Order_Utils.return_order_array(value['buy_summary'])
        current_item.sell_summary = Order_Utils.return_order_array(value['sell_summary'])

update_bazaar_data()

print(f'{item_array[index_of_item_in_item_arr['BOOSTER_COOKIE']].buy_summary[0].price_per_unit:,}')

bz_arr = return_bazaar_array()
for item in bz_arr:
    if len(item.buy_summary) > 0:
        print(f'{item.internal_name} = {item.buy_summary[0].price_per_unit:,}')
    else:
        print(item.internal_name)

print(item_array[index_of_item_in_item_arr['ENCHANTED_DIAMOND']])

"""
we will have something with multithreading later for updating bazaar prices.
but for now assemble the crafting system and compare prices. 
"""

"""
we will probably scrape data for the accurate crafting recipes
"""