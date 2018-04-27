from models import *
from hunter import Hunter
from errors import InvalidInventoryError
import random
import argparse



def get_options():
    parser = argparse.ArgumentParser(prog='bloodborne-rundomizer')
    parser.add_argument('-no_bigguns', action='store_true', help='Remove all firearms with a strength requirement of 27+ from item pool.')
    parser.add_argument('-no_chalice', action='store_true', help='Remove chalice dungeon items from item pool.')
    parser.add_argument('-no_fashion', action='store_true', help='Remove fashionable items from item pool. You fiend.')
    parser.add_argument('-fashion', action='store_true', help='Choose a random armor piece per slot across all armor sets.')
    parser.add_argument('-no_torches', action='store_true', help="Remove Torch and Hunter's Torch from item pool")
    parser.add_argument('-no_shields', action='store_true', help='Remove Wooden Shield and Loch Shield from item pool')
    return parser.parse_args()


def populate_weapons():
    weapons = []
    with open('data/weapons.txt') as f:
        for row in f:
            if row[0] != '#':
                weapon_details = row.split(',')
                name = weapon_details[0].strip()
                chalice = weapon_details[1].strip()
                weapon_type = weapon_details[2].strip()
                requirements = dict([('str', int(weapon_details[3].strip())), ('skl', int(weapon_details[4].strip())), ('blt', int(weapon_details[5].strip())), ('arc', int(weapon_details[6].strip()))])
                weapons.append(Weapon(name, weapon_type, chalice, requirements))
    return weapons


def populate_armor():
    armor = []
    with open('data/armor.txt') as f:
        for row in f:
            if row[0] != '#':
                armor_details = row.split(',')
                name = armor_details[0].strip()
                chalice = armor_details[1].strip()
                armor_type = armor_details[2].strip()
                armor_set = armor_details[3].strip()
                fashionable = armor_details[4].strip()
                armor.append(Armor(name, armor_type, chalice, armor_set, fashionable))
    return armor


def populate_armor_sets(armor):
    armor_sets = []
    for piece in armor:
        if (piece.armor_set not in armor_sets) and (piece.armor_set != 'NO_SET'):
            armor_sets.append(piece.armor_set)
    return armor_sets


def filter_equipment(equipment, options):
    if options.no_chalice:
        equipment = remove_chalice_items(equipment)
    return equipment


def filter_weapons(weapons, options):
    weapons = filter_equipment(weapons, options)
    if options.no_bigguns:
        weapons = remove_big_guns(weapons)
    if options.no_torches:
        weapons = remove_torches(weapons)
    if options.no_shields:
        weapons = remove_shields(weapons)
    return weapons


def filter_armor(armor, options):
    armor = filter_equipment(armor, options)
    if options.no_fashion:
        armor = remove_fashionable_items(armor)
    return armor


def remove_chalice_items(equipment):
    new_equipment = []
    for item in equipment:
        if item.chalice != 'True':
            new_equipment.append(item)
    return new_equipment


def remove_big_guns(weapons):
    new_weapons = []
    for piece in weapons:
        if piece.slot != 'Firearm' or piece.requirements['str'] < 27:
            new_weapons.append(piece)
    return new_weapons


def remove_torches(weapons):
    torches = ['Torch', "Hunter's Torch"]
    new_weapons = []
    for piece in weapons:
        if piece.name not in torches:
            new_weapons.append(piece)
    return new_weapons

def remove_shields(weapons):
    shields = ['Wooden Shield', 'Loch Shield']
    new_weapons = []
    for piece in weapons:
        if piece.name not in shields:
            new_weapons.append(piece)
    return new_weapons


def remove_fashionable_items(armor):
    new_armor = []
    for piece in armor:
        if piece.fashionable != 'True':
            new_armor.append(piece)
    return new_armor


def take_random_from_list(items):
    return items[random.randint(0, len(items) - 1)]


def choose_equipment_for_slot(equipment, slot):
    chosen = False
    selected = None
    while not chosen:
        selected = take_random_from_list(equipment)
        if selected.slot == slot:
            chosen = True
    return selected


def choose_armor_set(armor):
    chosen_set = take_random_from_list(populate_armor_sets(armor))
    set_pieces = []
    for piece in armor:
        if piece.armor_set == chosen_set:
            set_pieces.append(piece)
    return set_pieces


def choose_all_weapons(options):
    weapons = filter_weapons(populate_weapons(), options)
    if not weapons:
        raise InvalidInventoryError('No suitable weapons found - please verify inventory file and filters')
    chosen_weapons = []
    for slot in Weapon.slots:
        chosen_weapons.append(choose_equipment_for_slot(weapons, slot))
    return chosen_weapons


def choose_all_armor(options):
    armor = filter_armor(populate_armor(), options)
    if not armor:
        raise InvalidInventoryError('No suitable armor found - please verify inventory file and filters')
    chosen_armor = []
    if options.fashion:
        for slot in Armor.slots:
            chosen_armor.append(choose_equipment_for_slot(armor, slot))
    else:
        chosen_armor = choose_armor_set(armor)
    return chosen_armor


def choose_all_equipment(options):
    equipment = []
    for weapon in choose_all_weapons(options):
        equipment.append(weapon)
    for armor in choose_all_armor(options):
        equipment.append(armor)
    return equipment


def main():
    Hunter(choose_all_equipment(get_options())).display_info()
    

if __name__ == '__main__':
    main()
