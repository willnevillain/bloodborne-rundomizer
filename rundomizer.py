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

def chooseItem(db_table, args):
    items = db_table.all()
    rand = random.randint(0, len(items) - 1)
    item = None
    chosen = False
    while not chosen:
        item = items[rand]
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
    print(args)

    db = TinyDB('data/db.json')
    weapon = chooseItem(db.table('trick_weapons'), args)
    firearm = chooseItem(db.table('firearms'), args)
    head = chooseItem(db.table('head_attire'), args)
    

    print(weapon)
    print(firearm)
    print(head)

if __name__ == '__main__':
    main()
