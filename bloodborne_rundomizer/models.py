class Item(object):
    def __init__(self, name):
        self.name = name

class Equipment(Item):
    def __init__(self, name, location):
        Item.__init__(self, name)
        self.location = location

class Armor(Equipment):
    def __init__(self, name, location, armor_type, fashionable):
        Equipment.__init__(self, name, location)
        self.armor_type = armor_type
        self.fashionable = fashionable

class Weapon(Equipment):
    def __init__(self, name, location, weapon_type, requirements):
        Equipment.__init__(self, name, location)
        self.weapon_type = weapon_type
        self.requirements = requirements
