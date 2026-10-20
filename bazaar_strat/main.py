from Item_Utils import Item
import Item_Utils as Item_utils
import sys
import time
import requests

BAZAAR_API = requests.get('https://api.hypixel.net/skyblock/bazaar').json()

item_array= Item_utils.return_item_array()