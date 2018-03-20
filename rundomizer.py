from tinydb import TinyDB

import random

plus = False
chalice = False

def chooseItem(db_table):
    items = db_table.all()
    rand = random.randint(0, len(items) - 1)
    return items[rand]

def main():
    db = TinyDB('data/db.json')
    weapon = chooseItem(db.table('trick_weapons'))
    firearm = chooseItem(db.table('firearms'))
    print(weapon)
    print(firearm)

if __name__ == '__main__':
    main()
