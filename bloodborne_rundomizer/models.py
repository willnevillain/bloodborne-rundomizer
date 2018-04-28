class Item(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Tool(Item):
    def __init__(self, name, requirements):
        Item.__init__(self, name)
        self.requirements = requirements

class Rune(Item):
    def __init__(self, name, covenant):
        Item.__init__(self, name)
        self.covenant = covenant

class Equipment(Item):
    def __init__(self, name, slot, chalice):
        Item.__init__(self, name)
        self.slot = slot
        self.chalice = chalice

class Armor(Equipment):
    slots = ['Head', 'Chest', 'Hand', 'Leg']
    def __init__(self, name, slot, chalice, armor_set):
        Equipment.__init__(self, name, slot, chalice)
        self.armor_set = armor_set

class Weapon(Equipment):
    slots = ['Trick', 'Firearm']
    def __init__(self, name, slot, chalice, requirements):
        Equipment.__init__(self, name, slot, chalice)
        self.requirements = requirements
