from models import *
from hunter import Hunter
from errors import InvalidInventoryError
import random
import argparse



def get_options():
    parser = argparse.ArgumentParser(prog='bloodborne-rundomizer')
    parser.add_argument('-no_bigguns', action='store_true', help='Remove all firearms with a strength requirement of 27+ from item pool.')
    parser.add_argument('-no_chalice', action='store_true', help='Remove chalice dungeon items from item pool.')
    parser.add_argument('-no_plus', action='store_true', help='Remove NG+ items from item pool.')
    parser.add_argument('-no_fashion', action='store_true', help='Remove fashionable items from item pool. You fiend.')
    return parser.parse_args()


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


def filter_equipment(equipment, options):
    if options.no_plus:
        equipment = remove_plus_items(equipment)
    if options.no_chalice:
        equipment = remove_chalice_items(equipment)
    return equipment


def filter_weapons(weapons, options):
    weapons = filter_equipment(weapons)
    if options.no_bigguns
        weapons = remove_big_guns(weapons)
    return weapons


def filter_armor(armor, options):
    armor = filter_equipment(armor)
    if options.no_fashion
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


def remove_big_guns(weapons):
    new_weapons = []
    for piece in weapons:
        if piece.weapon_type != 'Firearm' or piece.requirements['str'] < 27:
            new_weapons.append(piece)
    return new_weapons


def remove_fashionable_items(armor):
    new_armor = []
    for piece in armor:
        if piece.fashionable != 'True':
            new_armor.append(piece)
    return new_armor


def choose_equipment(equipment):
    return equipment[random.randint(0, len(equipment) - 1)]


def choose_weapon(options):
    weapons = filter_weapons(populate_weapons(), options)
    if not weapons:
        raise InvalidInventoryError('No suitable weapons found - please verify inventory file and filters')
    return choose_equipment(weapons)


def choose_armor(options):
    armor = filter_armor(populate_armor(), options)
    if not armor:
        raise InvalidInventoryError('No suitable armor found - please verify inventory file and filters')
    return choose_equipment(armor)


def main():
    options = get_options()
    

if __name__ == '__main__':
    main()
