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

    def __init__(self, commerce_type: str, internal_name: str, craft_parameters: dict, npc_sellable: int):
        self.commerce_type = commerce_type
        """ 
        commerce_type:
            'bazaar', 'auction', 'None', 'soulbound'
        """
        self.internal_name = internal_name
        self.craft_parameters = craft_parameters
        self.npc_sellable = npc_sellable
        """
        if npc_sellable is 0 then Item is not npc-sellable
        """
        self.latest_bazaar_price = None

    def Return_Dict(self):
        data_to_return = {
            'commerce_type': self.commerce_type,
            'internal_name': self.internal_name,
            'craft_parameters': self.craft_parameters,
            'npc_sellable': self.npc_sellable,
        }


def get_number_and_internal_name_for_NEU_item_DB(string):
    internal_name = ""
    number = 0
    for letter in string:
        if letter != ':':
            internal_name += letter
        else:
            number = int(string[string.index(letter) + 1:])

            return number, internal_name

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
    if internal_name in auctioned:
        return 'auction'
    for item in ITEM_API['item']:
        if item.get('id') == internal_name:
            if item.get('can_auction')!= None:
                if item['can_auction'] == True:
                    return 'auction'
            if item.get('soulbound') != None:
                return 'soulbound'
    return 'None'

def return_npc_sellable(internal_name):
    for item in ITEM_API['item']:
            if item.get('id') == internal_name:
                if item.get('npc_sell_price')!= None:
                    return item['npc_sell_price']
                return 0
        

for file_path in dir_path.iterdir():

    with open(file_path, "r")as f:

        current = json.load(f)

        #if current['internalname'] in bazaarable or current['internalname'] in auctioned:
        print(current['internalname'])
        craft_parameters = {}
        if current.get("recipe") != None:
            craft_parameters['count'] = 1
            for key, string in current["recipe"].items():
                if key == "count":
                    craft_parameters['count'] = int(string)
                    continue
                if string != "":
                    print(file_path)
                    amount, internal_name = get_number_and_internal_name_for_NEU_item_DB(string)
                    print(f'amount = {amount}\ninternal_name = {internal_name}')
                    if craft_parameters.get(internal_name) is None:
                        craft_parameters[internal_name] = amount
                    else:
                        craft_parameters[internal_name] += amount
                    
            print(craft_parameters)

        commerce_type = return_commerce_type(current['internalname'])
        npc_sell_price = return_npc_sellable(current['internalname'])
        Item(commerce_type, current['internalname'], craft_parameters, npc_sell_price)



            #--------------
            # if len(current['internalname']) is 1:
            #     print(file_path)

# if 'Z' in bazaarable:
#     print(bazaarable.index('Z'))