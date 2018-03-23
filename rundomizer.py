from tinydb import TinyDB
from sys import argv
from hunter import Hunter

import random

def getopts(argv):
    opts = []
    while(argv):
        if argv[0][0] == '-':
            opts.append(argv[0][1:])
        argv = argv[1:]
    return opts

def list_options():
    options = {
        'plus': 'Allows items found only in NG+ to be chosen.',
        'chalice': 'Allows items found only in chalice dungeons to be chosen.',
        'fashion': 'Armor will include items with no set, and less functional armor.',
        'all': 'Alias to enable plus, chalice and fashion options.',
        'set': 'All armor chosen will be from same set. To be implemented! :)', #to be implemented
        'dual': 'Two trick weapons and two firearms will be chosen.'
    }
    for opt in options:
        print('-' + opt + '  :  ' + options[opt])

def choose_item(db_table, args):
    items = db_table.all()
    item = None
    chosen = False
    items_seen = []
    while not chosen:
        rand = random.randint(0, len(items) - 1)
        item = items[rand]
        if item['name'] not in items_seen:
            items_seen.append(item['name'])
        if len(items_seen) >= len(items):
            return {
                'message': 'Saw all items and found none suitable! Verify data files and parameters!'
            }
        if 'all' not in args:
            if item['plus'] == 'True' and 'plus' not in args:
                continue
            if item['chalice'] == 'True' and 'chalice' not in args:
                continue
            if 'fashion' in item and item['fashion'] == 'True' and 'fashion' not in args:
                continue
        chosen = True
    return items[rand]

def main():
    args = getopts(argv)

    if 'help' in args:
        list_options()
        return

    db = TinyDB('data/db.json')
    chosen_items = {}
    for table_name in db.tables():
        if table_name == '_default':
            continue
        table = db.table(table_name)
        if 'dual' in args and table_name in ['trick_weapons', 'firearms']:
            weapon = choose_item(table, args)
            chosen_items[weapon['subtype']] = [weapon]
            #fixme - same weapon can be chosen twice
            weapon = choose_item(table, args)
            chosen_items[weapon['subtype']].append(weapon)
        else:
            item = choose_item(table, args)
            chosen_items[item['subtype']] = item
    
    hunter = Hunter('Build', chosen_items)
    hunter.add_items(chosen_items)
    hunter.calculate_stats()
    print(hunter.items)
    print(hunter.req_stats)
    hunter.display_info()
    
    

if __name__ == '__main__':
    main()
