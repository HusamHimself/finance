"""
we go through each file in the NEU thing and we check if the item is bazaarable or auctionable
if it is any of these: we somehow write in that the item is a result of some amount of some many itmes through a craft.
then from then on we pull ah and bazaar data and output items that are insanely more expensive after being crafted.
"""

from pathlib import Path
import os
import json
import requests


class Item:
    """
    Decided to merge item classes, building cleaner.
    craft_parameters will be a dictionary data type
    it can have a key that says if empty or not, so that will improve readability
    """

    def __init__(self, commerce_type: str, internal_name: str, craft_parameters: dict, npc_sellable: bool):
        self.commerce_type = commerce_type
        """ 
        commerce_type:
            'bazaar', 'auction', 'None', 'soulbound'
        """
        self.internal_name = internal_name
        self.craft_parameters = craft_parameters
        self.npc_sellable = npc_sellable
        self.npc_sell_price = None
        self.latest_bazaar_price = None

    def Return_Dict(self):
        data_to_return = {
            'commerce_type': self.commerce_type,
            'internal_name': self.internal_name,
            'craft_parameters': self.craft_parameters,
            'npc_sellable': self.npc_sellable,
            'npc_sell_price': self.npc_sell_price
        }


def get_number_and_internal_name_for_NEU_item_DB(string):
    internal_name = ""
    number = 0
    for letter in string:
        if letter != ':':
            internal_name += letter
        else:
            number = int(string[string.index(letter) + 1:])

            return number, internal_name, 

dir_path = Path("NotEnoughUpdates-REPO-master/items")

with open('data/bazaarable.json', 'r')as f:
    i = json.load(f)
    bazaarable = i['internal_name']

with open('data/auctioned.json')as f:
    i = json.load(f)
    auctioned = i['internal_name']

ITEM_API = requests.get('https://api.hypixel.net/resources/skyblock/items').json()

def return_commerce_type(internal_name) -> str:  
    """
    must return one of the following: 'bazaar', 'auction', 'None', 'soulbound'
    """
    if internal_name in bazaarable:
        return 'bazaar'

for file_path in dir_path.iterdir():

    with open(file_path, "r")as f:

        current = json.load(f)

        #if current['internalname'] in bazaarable or current['internalname'] in auctioned:
        print(current['internalname'])

        if current.get("recipe") != None:
            crafting_cost = {}
            crafting_cost['count'] = 1
            for key, string in current["recipe"].items():
                if key == "count":
                    crafting_cost['count'] = int(string)
                    continue
                if string != "":
                    print(file_path)
                    amount, internal_name = get_number_and_internal_name_for_NEU_item_DB(string)
                    print(f'amount = {amount}\ninternal_name = {internal_name}')
                    if crafting_cost.get(internal_name) is None:
                        crafting_cost[internal_name] = amount
                    else:
                        crafting_cost[internal_name] += amount
                    
            print(crafting_cost)

            Item()



            #--------------
            # if len(current['internalname']) is 1:
            #     print(file_path)

# if 'Z' in bazaarable:
#     print(bazaarable.index('Z'))