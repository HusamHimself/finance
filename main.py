import requests

get = requests.get('https://api.hypixel.net/skyblock/bazaar').json()
print(get['products']['ENCHANTED_DIAMOND']['quick_status'])
"""
The data structure is pretty simple.
we have success and a last updated stat at the root
then we have products
inside we have products with their name
inside a product's name is the product id with a sell summary and buy summary for the product
with a quick status part that also has productId with sell price sellvolume sellmovingweek wellorders and the same thing for buy

"""