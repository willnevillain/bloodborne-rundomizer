class Item(object):
    def __init__(self, name):
        self.name = name

class Equipment(Item):
    def __init__(self, name, location):
        Item.__init__(self, name)
        self.location = location
    def __str__(self):
        return self.name


class Armor(Equipment):

    types = ['Head', 'Chest', 'Hand', 'Leg']

    def __init__(self, name, location, armor_type, armor_set, fashionable):
        Equipment.__init__(self, name, location)
        self.armor_type = armor_type
        self.armor_set = armor_set
        self.fashionable = fashionable


class Weapon(Equipment):

    types = ['Trick', 'Firearm']

    def __init__(self, name, location, weapon_type, requirements):
        Equipment.__init__(self, name, location)
        self.weapon_type = weapon_type
        self.requirements = requirements
