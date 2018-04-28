from models import *

class Hunter:

    
    def __init__(self, equipment, items):
        self.equipped = self.bind_equipment(equipment)
        self.tools = self.bind_item_type(items, Tool)
        self.runes = self.bind_item_type(items, Rune)
        self.req_stats = self.calculate_stats()


    def bind_equipment(self, equipment):
        equipped = {}
        for piece in equipment:
            equipped[piece.slot] = piece
        return equipped


    def bind_item_type(self, items, item_class):
        items_of_type = []
        for item in items:
            if isinstance(item, item_class):
                items_of_type.append(item)
        return items_of_type


    def calculate_stats(self):
        req_stats = {}
        for piece in self.equipped.values():
            if isinstance(piece, Weapon):
                for stat in piece.requirements:
                    if (stat not in req_stats) or (req_stats[stat] < piece.requirements[stat]):
                        req_stats[stat] = piece.requirements[stat]
        for tool in self.tools:
            for stat in tool.requirements:
                if (stat not in req_stats) or (req_stats[stat] < tool.requirements[stat]):
                    req_stats[stat] = tool.requirements[stat]
        return req_stats

                
    def display_info(self):
        for slot, piece in self.equipped.items():
            print(slot + ': ' + str(piece))
        if self.tools:
            print('Tools: ' + str(self.tools))
        if self.runes:
            print('Runes: ' + str(self.runes))
        print('Stat requirements: ' + str(self.req_stats))
