class Item(object):
    def __init__(self, name):
        self.name = name

class Equipment(Item):
    def __init__(self, name, slot, chalice):
        Item.__init__(self, name)
        self.slot = slot
        self.chalice = chalice
    def __str__(self):
        return self.name

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
