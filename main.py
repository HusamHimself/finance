import requests

#BAZAAR_API = requests.get('https://api.hypixel.net/skyblock/bazaar').json()
#print(BAZAAR_API['products']['ENCHANTED_DIAMOND']['quick_status'])

"""
The data structure is pretty simple.
we have success and a last updated stat at the root
then we have products
inside we have products with their name
inside a product's name is the product id with a sell summary and buy summary for the product
with a quick status part that also has productId with sell price sellvolume sellmovingweek wellorders and the same thing for buy
"""
# n = 0
# for productId, product in BAZAAR_API['products'].items():
#     print(product)
#     n += 1
#     if n == 2:
#         break

#ELECTION_API = requests.get('https://api.hypixel.net/resources/skyblock/election').json()
"""
The data structure is also pretty simple
at the root we get the basic stuff of last updated, mayor, current, and success.
inside mayor we get their personal data, like key, name, perks, and minister.
then inside that we get election in which we get the election that put them in power, with year and candidates with their personal info

then we get current which is about the current election that is happening which has year and candidates
candidate objects have the same structure as the other mayor's election objects
"""
#print(ELECTION_API)

# for productId in ELECTION_API['current']['candidates']:
#     print(productId['name'], end=' = ')
#     print(f'{productId['votes'] :,}')

ITEM_API = requests.get('https://api.hypixel.net/resources/skyblock/items').json()
"""
New form of data for all the items in skyblock and info about them
this will probably act as some sort of verifier for the general program.
The actual data assembly will be off of NEU and that will be it.
for every item we will declare a class, and inside of that class we can write about how they are tradable or soulbound
and if they are tradable are they bazaarable or auctionable.
Inside NEU we also get a unique data structure for displaying if items are craftable and how they are sourced in general.
there is also a very unique way to see how items get upgraded with essense.
"""

#AUCTION_API = requests.get('https://api.hypixel.net/skyblock/auctions').json()

"""
Now we have reached the point in which we decide to sort out the crafting profitability system
which can be coin wise or margin wise but that is a topic for later discussion.
I'll start out by listing all bazaar tradable items with their 'internal names' as the devs behind NEU would put them.
then I'll also add all auction housable items and then through that we will construct the mega data set that will have each item
tied up to the price of another with crafting.
"""

"""
process news fast as a feature with LLMs lol
"""