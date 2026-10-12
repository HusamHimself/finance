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
"""
The data structure is also pretty simple
at the root we get the basic stuff of last updated, mayor, current, and success.
inside mayor we get their personal data, like key, name, perks, and minister.
then inside that we get election in which we get the election that put them in power, with year and candidates with their personal info

then we get current which is about the current election that is happening which has year and candidates
candidate objects have the same structure as the other mayor's election objects
"""
#print(gettwo)

for productId in gettwo['current']['candidates']:
    print(productId['name'], end=' = ')
    print(productId['votes'])