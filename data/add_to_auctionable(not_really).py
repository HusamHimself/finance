import requests
import base64
from nbt import nbt
import io
import time
import json


auctioned = set()

AUCTION_API = requests.get(f'https://api.hypixel.net/skyblock/auctions?page=0').json()

total_pages_to_loop_over = requests.get('https://api.hypixel.net/skyblock/auctions?page=0').json()['totalPages'] 

for i in range(0, total_pages_to_loop_over):
    z = 0
    try:
        CURRENT_AUCTION_PAGE = requests.get(f'https://api.hypixel.net/skyblock/auctions?page={i}').json()
    except Exception:
        time.sleep(1)
        try:   
            CURRENT_AUCTION_PAGE = requests.get(f'https://api.hypixel.net/skyblock/auctions?page={i}').json()
        except Exception:
            break

    for item in CURRENT_AUCTION_PAGE['auctions']:
        raw_data = base64.b64decode(item['item_bytes'])
        nbt_file = nbt.NBTFile(fileobj=io.BytesIO(raw_data))
        item_id = nbt_file['i'][0]['tag']['ExtraAttributes']['id'].value
        auctioned.add(item_id)
        print(f'index {z}: {item_id} with the rarity of {item['tier']}')
        z+=1
    time.sleep(0.5)

with open('auctioned.json', 'w')as f:
    json.dump({'internal_name': list(auctioned)}, f, indent=2)

print(auctioned)