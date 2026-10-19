import requests
import json

ITEM_API = requests.get('https://api.hypixel.net/resources/skyblock/items').json()

special_cases = ['SWORD_OF_LIVE_RELOADING', 'HELMET_OF_LIVE_RELOADING', 'KUUDRA_WASHING_MACHINE', "ANITA_TALISMAN"]

with open('data/auctioned.json')as f:
    i = json.load(f)
    auctioned = i['internal_name']

with open('data/bazaarable.json', 'r')as f:
    i = json.load(f)
    bazaarable = i['internal_name']

for item in ITEM_API['items']:
    if item.get('soulbound') == 'COOP' or item.get('soulbound') == 'SOLO':
        continue

    if item.get('category') in ('FARMING_TOOL', 'SACK'):
        continue
    if item.get('generator')!= None:
        continue

    if item.get('can_auction') is None:
        if item['id'] in bazaarable or item['id'] in special_cases:
            continue
        if item['id'] not in auctioned:
            print(item['id'],end=': ')
            print(item['name'])