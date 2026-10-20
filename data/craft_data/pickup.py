import json
"""
The internal names having numbers is a feature not a bug.
"""
all_items = []
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

    def return_dict(self):
        data_to_return = {
            'commerce_type': self.commerce_type,
            'internal_name': self.internal_name,
            'craft_parameters': self.craft_parameters,
            'npc_sellable': self.npc_sellable,
        }
        return data_to_return

with open('data/itemz.json', 'r')as f:
    temp = json.load(f)
    for item in temp['objects']:
        x = Item(item['commerce_type'], item['internal_name'], item['craft_parameters'], item['npc_sellable'])
        all_items.append(x)

def find(name: str):
    for object in all_items:
        if object.internal_name == name:
            return object

print(find('COAL_GENERATOR_1').craft_parameters)

for object in all_items:
    if object.npc_sellable is not 0:
        print(f'{object.internal_name} : {object.npc_sellable:,}')