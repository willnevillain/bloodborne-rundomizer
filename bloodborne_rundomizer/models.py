class Item(object):
    def __init__(self, name):
        self.name = name

class Equipment(Item):

    def __init__(self, name, location, slot):
        Item.__init__(self, name)
        self.location = location
        self.slot = slot

    def __str__(self):
        return self.name


class Armor(Equipment):

    slots = ['Head', 'Chest', 'Hand', 'Leg']

    def __init__(self, name, location, slot, armor_set, fashionable):
        Equipment.__init__(self, name, location, slot)
        self.armor_set = armor_set
        self.fashionable = fashionable


class Weapon(Equipment):

    slots = ['Trick', 'Firearm']

    def __init__(self, name, location, slot, requirements):
        Equipment.__init__(self, name, location, slot)
        self.requirements = requirements
