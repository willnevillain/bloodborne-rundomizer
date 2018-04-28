from models import *

class Hunter:
    
    def __init__(self, equipment, items):
        self.equipped = self.bind_equipment(equipment)
        self.items = items
        self.req_stats = self.calculate_stats()

    def bind_equipment(self, equipment):
        equipped = {}
        for piece in equipment:
            equipped[piece.slot] = piece
        return equipped

    def calculate_stats(self):
        req_stats = {}
        for piece in self.equipped.values():
            if isinstance(piece, Weapon):
                for stat in piece.requirements:
                    if (stat not in req_stats) or (req_stats[stat] < piece.requirements[stat]):
                        req_stats[stat] = piece.requirements[stat]
        for item in self.items:
            if isinstance(item, Tool):
                for stat in item.requirements:
                    if (stat not in req_stats) or (req_stats[stat] < item.requirements[stat]):
                        req_stats[stat] = item.requirements[stat]
        return req_stats
                
    def display_info(self):
        for slot, piece in self.equipped.items():
            print(slot + ': ' + str(piece))
        print('Items: ' + str(self.items))
        print('Stat requirements: ' + str(self.req_stats))
