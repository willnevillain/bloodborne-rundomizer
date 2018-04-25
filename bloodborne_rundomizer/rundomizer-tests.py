import unittest
import rundomizer
from models import Weapon, Armor

class TestFilters(unittest.TestCase):

    def test_remove_plus_armor(self):
        all_armor = rundomizer.populate_armor()
        filtered = rundomizer.remove_plus_items(all_armor)
        for piece in filtered:
            print(piece)
            self.assertTrue(piece.location != 'NG+')
        self.assertTrue(len(filtered) < len(all_armor))
            

    def test_remove_plus_weapons(self):
        all_weapons = rundomizer.populate_weapons()
        filtered = rundomizer.remove_plus_items(all_weapons)
        for weapon in filtered:
            print(weapon)
            self.assertTrue(weapon.location != 'NG+')
        self.assertTrue(len(filtered) < len(all_weapons))
            

    def test_remove_big_guns(self):
        all_weapons = rundomizer.populate_weapons()
        filtered = rundomizer.remove_big_guns(all_weapons)
        for weapon in filtered:
            if weapon.slot == 'Firearm':
                self.assertTrue(weapon.requirements['str'] < 27)
        self.assertTrue(len(filtered) < len(all_weapons))

    
            


if __name__ == '__main__':
    unittest.main()
