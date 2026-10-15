"""
we go through each file in the NEU thing and we check if the item is bazaarable or auctionable
if it is any of these: we somehow write in that the item is a result of some amount of some many itmes through a craft.
then from then on we pull ah and bazaar data and output items that are insanely more expensive after being crafted.
"""

from pathlib import Path
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




dir_path = Path(r"\NotEnoughUpdates-REPO-master\items")

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

            # if len(current['internalname']) is 1:
            #     print(file_path)

# if 'Z' in bazaarable:
#     print(bazaarable.index('Z'))