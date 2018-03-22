from tinydb import TinyDB
from sys import argv

import random

def getopts(argv):
    opts = []
    while(argv):
        if argv[0][0] == '-':
            opts.append(argv[0][1:])
        argv = argv[1:]
    return opts

def choose_item(db_table, args):
    items = db_table.all()
    item = None
    chosen = False
    items_seen = []
    while not chosen:
        rand = random.randint(0, len(items) - 1)
        item = items[rand]
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

    db = TinyDB('data/db.json')
    chosen_items = []
    for table_name in db.tables():
        if table_name == '_default':
            continue
        table = db.table(table_name)
        chosen_items.append(choose_item(table, args))
    
    chosen_items_organized = {}
    for item in chosen_items:
        chosen_items_organized[item['subtype']] =  item['name']

    print(chosen_items_organized)
    

if __name__ == '__main__':
    main()
