from models import Weapon, Armor

class Hunter:
    
    def __init__(self, equipment):
        self.equipment = []
        self.equipped = {}
        self.req_stats = {}

        self.bind_equipment(equipment)

    def bind_equipment(self, equipment):
        for piece in equipment:
            self.equipped[piece.slot] = piece
            
                
    def display_info(self):
        for slot, piece in self.equipped.items():
            print(slot + ': ' + str(piece))
