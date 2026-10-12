import requests

get = requests.get('https://api.hypixel.net/skyblock/bazaar').json()
# print(get['products']['ENCHANTED_DIAMOND']['quick_status'])

"""
The data structure is pretty simple.
we have success and a last updated stat at the root
then we have products
inside we have products with their name
inside a product's name is the product id with a sell summary and buy summary for the product
with a quick status part that also has productId with sell price sellvolume sellmovingweek wellorders and the same thing for buy
"""
# n = 0
# for productId, product in get['products'].items():
#     print(product)
#     n += 1
#     if n == 2:
#         break

gettwo = requests.get('https://api.hypixel.net/resources/skyblock/election').json()
print(gettwo)