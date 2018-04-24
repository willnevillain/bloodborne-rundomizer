from tinydb import TinyDB
from sys import argv
from models import *
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
        'dual': 'Two trick weapons and two firearms will be chosen.',
        'no-big-guns': 'Guns requiring 27+ strength will be not be chosen'
    }
    for opt in options:
        print('-' + opt + '  :  ' + options[opt])


def populate_weapons():
    weapons = []
    with open('data/weapons.txt') as f:
        for row in f:
            if row[0] != '#':
                weapon_details = row.split(',')
                name = weapon_details[0].strip()
                location = weapon_details[1].strip()
                weapon_type = weapon_details[2].strip()
                requirements = dict([('str', int(weapon_details[3].strip())), ('skl', int(weapon_details[4].strip())), ('blt', int(weapon_details[5].strip())), ('arc', int(weapon_details[6].strip()))])
                weapons.append(Weapon(name, location, weapon_type, requirements))
    return weapons

def populate_armor():
    armor = []
    with open('data/armor.txt') as f:
        for row in f:
            if row[0] != '#':
                armor_details = row.split(',')
                name = armor_details[0].strip()
                location = armor_details[1].strip()
                armor_type = armor_details[2].strip()
                armor_set = armor_details[3].strip()
                fashionable = armor_details[4].strip()
                armor.append(Armor(name, location, armor_type, armor_set, fashionable))
    return armor

def execute_weapon_filters(weapons, args):
    if 'no-plus' in args:
        weapons = remove_plus_items(weapons)
    if 'no-chalice' in args:
        weapons = remove_chalice_items(weapons)
    if 'no-big-guns' in args:
        weapons = remove_big_guns(weapons)
    return weapons

def execute_armor_filters(armor, args):
    if 'no-plus' in args:
        armor = remove_plus_items(armor)
    if 'no-chalice' in args:
        armor = remove_chalice_items(armor)
    if 'no-fashion' in args:
        armor = remove_fashionable_items(armor)
    return armor

def remove_plus_items(equipment):
    new_equipment = []
    for item in equipment:
        if item.location != 'NG+':
            new_equipment.append(item)
    return new_equipment

def remove_chalice_items(equipment):
    new_equipment = []
    for item in equipment:
        if item.location != 'Chalice':
            new_equipment.append(item)
    return new_equipment

def remove_fashionable_items(armor):
    new_armor = []
    for piece in armor:
        if piece.fashionable != 'True':
            new_armor.append(piece)
    return new_armor

def remove_big_guns(weapons):
    new_weapons = []
    for piece in weapons:
        if piece.weapon_type != 'Firearm' or piece.requirements['str'] < 27:
            new_weapons.append(piece)
    return new_weapons
            

def populate_items_from_db():
    all_items = {}
    db = TinyDB('data/db.json')
    for table_name in db.tables():
        if table_name != '_default':
            all_items[table_name] = db.table(table_name).all()
    return all_items


def remove_undesired_items(all_items, args):
    relevant_args = ['plus', 'chalice', 'fashion']
    for item_type, all_items_of_type in all_items.items():
        to_be_removed = []
        for item in all_items_of_type:
            for arg in relevant_args:
                if arg in item:
                    if item[arg] == 'True' and arg not in args:
                        print("removing item " + item['name'] + " due to missing flag " + arg)
                        to_be_removed.append(item)
                        break
            if item_type == 'firearms' and 'no-big-guns' in args:
                if int(item['str_req']) >= 27:
                    print("removing big gun: " + str(item))
                    to_be_removed.append(item)
        for item in to_be_removed:
            all_items_of_type.remove(item)




def choose_item(items, args):
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
        chosen = True
    return items[rand]


def choose_two_items(items, args):
    both_items = [choose_item(items, args)]
    item = None
    chosen = False
    while not chosen:
        item = choose_item(items, args)
        if item in both_items:
            continue
        chosen = True
    both_items.append(item)
    return both_items


def main():
    args = getopts(argv)

    if 'help' in args:
        list_options()
        return
    
    all_items = populate_items_from_db()
    remove_undesired_items(all_items, args)
    chosen_items = {}
    for item_type, all_items_of_type in all_items.items():
        if 'dual' in args and item_type in ['trick_weapons', 'firearms']:
            weapons = choose_two_items(all_items_of_type, args)
            chosen_items[weapons[0]['subtype']] = weapons
        else:
            item = choose_item(all_items_of_type, args)
            chosen_items[item['subtype']] = item
    
    hunter = Hunter('Build', chosen_items)
    hunter.add_items(chosen_items)
    hunter.calculate_stats()
    hunter.display_info()
    

if __name__ == '__main__':
    main()
