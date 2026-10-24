import json

class Item:
    """
    Decided to merge item classes, building cleaner.
    craft_parameters will be a dictionary data type
    it can have a key that says if empty or not, so that will improve readability
    """

    def __init__(self, commerce_type: str, internal_name: str, craft_parameters, npc_sellable: int):
        self.commerce_type = commerce_type
        """ 
        commerce_type:
            'bazaar', 'auction', 'None', 'soulbound'
        """
        self.internal_name = internal_name
        self.craft_parameters = craft_parameters
        """
        craft parameters can either be arrays for multiple crafting recipes or a lil dictionary 
        """
        self.npc_sellable = npc_sellable

        """
        will be full of Order objects.
        the priority will be determined by the index in the array.
        """
        self.buy_summary : list = None
        self.sell_summary : list = None

    def __str__(self):
            return f'Item({self.commerce_type}, {self.internal_name}, {self.craft_parameters}, {self.npc_sellable})'

    def return_dict(self):
        data_to_return = {
            'commerce_type': self.commerce_type,
            'internal_name': self.internal_name,
            'craft_parameters': self.craft_parameters,
            'npc_sellable': self.npc_sellable,
        }
        return data_to_return

    def priority_buy_order(self) -> int | float:
        if self.commerce_type != 'bazaar':
            raise TypeError("Item commerce type must be bazaar for using 'priority_buy_order' method.")
        try:
            return self.sell_summary[0].price_per_unit
            
        except IndexError:
            return -999999999999999999

    def priority_sell_order(self) -> int | float:
        if self.commerce_type != 'bazaar':
            raise TypeError("Item commerce type must be bazaar for using 'priority_sell_order' method.")
        try:
            return self.buy_summary[0].price_per_unit
        except IndexError:
            return 999999999999999999
    
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