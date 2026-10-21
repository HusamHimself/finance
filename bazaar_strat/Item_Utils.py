import json

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
        self.latest_bazaar_data = None
        self.latest_bazaar_data : dict
        """
        In a sense that the bazaar data will be the raw data that hypixel sends about buy and sell orders.
        """

    def return_dict(self):
        data_to_return = {
            'commerce_type': self.commerce_type,
            'internal_name': self.internal_name,
            'craft_parameters': self.craft_parameters,
            'npc_sellable': self.npc_sellable,
        }
        return data_to_return

def save_item_array(arr : list, filename='Item_Objects.json', prior_path='data/') -> None:
    temp_arr = []
    for item in arr:
        temp_arr.append(item.return_dict())
    temp_dict = {}
    temp_dict['objects'] = temp_arr
    with open(prior_path + filename, 'w')as f:
        json.dump(temp_dict, f, indent=4)

def return_item_array(filename='Item_Objects.json', prior_path='data/')-> list:
    arr_to_return = []
    with open(prior_path + filename, 'r')as f:
        temp_dict = json.load(f)
        for item in temp_dict['objects']:
            temp_object = Item(item['commerce_type'], item['internal_name'], item['craft_parameters'], item['npc_sellable'])
            arr_to_return.append(temp_object)
    return arr_to_return