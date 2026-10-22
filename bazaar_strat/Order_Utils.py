"""
utilities for the order class for orders in the bz
determine volume of an item and stuff

it should rebuild itself every time we update the bazaar prices, it'll get assembled by passing in the literal
array of the buy and sell orders from the bz and from that we assemble what the buy and sell is looking like for an item.
maybe it should be a part of the normal item class idk.

"""

sample = [[{'amount': 248514, 'pricePerUnit': 1265.5, 'orders': 4},
            {'amount': 49787, 'pricePerUnit': 1265.3, 'orders': 1},
            {'amount': 71000, 'pricePerUnit': 1265.0, 'orders': 2},
            {'amount': 349428, 'pricePerUnit': 1264.9, 'orders': 5},
            {'amount': 57355, 'pricePerUnit': 1263.3, 'orders': 3}, 
            {'amount': 36520, 'pricePerUnit': 1262.5, 'orders': 1}, 
            {'amount': 4705, 'pricePerUnit': 1262.4, 'orders': 1}, 
            {'amount': 17299, 'pricePerUnit': 1261.1, 'orders': 2}, 
            {'amount': 18138, 'pricePerUnit': 1255.0, 'orders': 1}, 
            {'amount': 41444, 'pricePerUnit': 1250.0, 'orders': 6}, 
            {'amount': 48996, 'pricePerUnit': 1247.9, 'orders': 1}, 
            {'amount': 17842, 'pricePerUnit': 1243.0, 'orders': 1}, 
            {'amount': 4700, 'pricePerUnit': 1225.8, 'orders': 2}, 
            {'amount': 30190, 'pricePerUnit': 1217.6, 'orders': 1}, 
            {'amount': 26431, 'pricePerUnit': 1000.0, 'orders': 18}]]

class Order:
    def __init__(self, amount : int, price_per_unit : list, orders : int):
        self.amount = amount
        self.price_per_unit = price_per_unit
        self.orders = orders

def return_order_array(data: list)-> list:
    array_to_return = []
    """
    priority will be determined by the index of the object in the array lmao
    """
    for order in data:
        x = Order(order['amount'], order['pricePerUnit'], order['orders'])
        array_to_return.append(x)
    return array_to_return