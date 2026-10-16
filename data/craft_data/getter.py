"""
we go through each file in the NEU thing and we check if the item is bazaarable or auctionable
if it is any of these: we somehow write in that the item is a result of some amount of some many itmes through a craft.
then from then on we pull ah and bazaar data and output items that are insanely more expensive after being crafted.
"""

from pathlib import Path
import os
import json


class Bazaar_Item:
    """
    the bazaar and auction class will interact with eachother.
    craft_parameters will be a dictionary data type
    it can have a key that says if empty or not, so that will improve readability
    """

    def __init__(self, internal_name, craft_parameters):
        self.internal_name = internal_name
        self.craft_parameters = craft_parameters
        self.latest_bazaar_price = None


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

for file_path in dir_path.iterdir():

    with open(file_path, "r")as f:

        current = json.load(f)

        if current['internalname'] in bazaarable or current['internalname'] in auctioned:
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




            #--------------
            # if len(current['internalname']) is 1:
            #     print(file_path)

# if 'Z' in bazaarable:
#     print(bazaarable.index('Z'))