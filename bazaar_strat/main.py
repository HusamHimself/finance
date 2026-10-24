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

def update_bazaar_data()-> None:
    for key, value in BAZAAR_API['products'].items():
        current_item = item_array[index_of_item_in_item_arr[key]]
        current_item.buy_summary = Order_Utils.return_order_array(value['buy_summary'])
        current_item.sell_summary = Order_Utils.return_order_array(value['sell_summary'])

def return_item(name) -> Item_Utils.Item:
    return item_array[index_of_item_in_item_arr[name]]

update_bazaar_data()

bz_arr = return_bazaar_array()

# for item in bz_arr:
#     if item.smallest_sell_order() < item.biggest_buy_order():
#         print(item)
#         print(f'highest buy order: {item.priority_buy_order()}')
#         print(f'lowest sell order: {item.priority_sell_order()}')
#         print('WOAHHHHHHHHHHHHHHHHH')
#         break

# return_item['ENCHANTMENT_GROWTH_5'].

"""
TODO 
Come up with a way to collect accurate crafting data for each item from the game's /recipe(item) function.
Map items and their prices together.(
Current item database and class especially the crafting attribute isn't reliable enough,
I suggest we make our own better reliable tailored and clean database from the skills we get from getting data directly from the game.)
Come up with a fast and reliable way to grab auction data from hypixel.
Check mapped prices on the bazaar and potentially the auction house.(
understand tax is a thing for both the BZ and AH.)
Return best profitd as a feature.
"""