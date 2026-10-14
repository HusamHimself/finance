import requests

auctioned = set()

total_pages_to_loop_over = requests.get('https://api.hypixel.net/skyblock/auctions?page=0').json()['totalPages'] + 1
print(total_pages_to_loop_over)

for i in range(0, total_pages_to_loop_over):

    CURRENT_AUCTION_API = requests.get(f'https://api.hypixel.net/skyblock/auctions?page={i}').json()
    z = 0

    for item in CURRENT_AUCTION_API['auctions']:
        print(f'index {z}: {item['item_name']}')
        z+= 1
    


# print(len(AUCTION_API['auctions']))
"""
training opportunity:
make a small Neural Network (duh) that predicts with the raw auction name of an item, what its 'internal_name' is
"""
