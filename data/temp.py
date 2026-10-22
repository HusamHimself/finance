import json

with open('bazaarable.json', 'r')as f:
    new = json.load(f)
    neww = new['internal_name']

if 'ENCHANTMENT_ULTIMATE_CROP_FEVER_5' in neww:
    print('YESSS')