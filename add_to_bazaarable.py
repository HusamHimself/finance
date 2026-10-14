import requests
import json

BAZAAR_API = requests.get('https://api.hypixel.net/skyblock/bazaar').json()
list_of_all_bazaarable_items = []
dict_of_all_bazaarable_items = {}
n = 0

for productId, product in BAZAAR_API['products'].items():
    # print(productId)
    list_of_all_bazaarable_items.append(productId)
    n += 1
    if n == 2:
        pass
        # break


dict_of_all_bazaarable_items['internal_name'] = list_of_all_bazaarable_items
    #'internalname' in NEU's data set btw

with open('bazaarable.json', 'w')as f:
    json.dump(dict_of_all_bazaarable_items, f, indent=1)

print(list_of_all_bazaarable_items)