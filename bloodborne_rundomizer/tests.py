import unittest
import rundomizer
from models import Weapon, Armor

class TestFilters(unittest.TestCase):

    def test_remove_plus_armor(self):
        all_armor = rundomizer.populate_armor()
        filtered = rundomizer.remove_plus_items(all_armor)
        for piece in filtered:
            self.assertTrue(piece.location != 'NG+')
        self.assertTrue(len(filtered) < len(all_armor))
            

    def test_remove_plus_weapons(self):
        all_weapons = rundomizer.populate_weapons()
        filtered = rundomizer.remove_plus_items(all_weapons)
        for weapon in filtered:
            self.assertTrue(weapon.location != 'NG+')
        self.assertTrue(len(filtered) < len(all_weapons))
            

    def test_remove_chalice_armor(self):
        all_armor = rundomizer.populate_armor()
        filtered = rundomizer.remove_chalice_items(all_armor)
        for piece in filtered:
            self.assertTrue(piece.location != 'Chalice')
        self.assertTrue(len(filtered) < len(all_armor))


    def test_remove_chalice_weapons(self):
        all_weapons = rundomizer.populate_weapons()
        filtered = rundomizer.remove_chalice_items(all_weapons)
        for weapon in filtered:
            self.assertTrue(weapon.location != 'Chalice')
        self.assertTrue(len(filtered) < len(all_weapons))


    def test_remove_big_guns(self):
        all_weapons = rundomizer.populate_weapons()
        filtered = rundomizer.remove_big_guns(all_weapons)
        for weapon in filtered:
            if weapon.slot == 'Firearm':
                self.assertTrue(weapon.requirements['str'] < 27)
        self.assertTrue(len(filtered) < len(all_weapons))

    
    def test_remove_fashionable_armor(self):
        all_armor = rundomizer.populate_armor()
        filtered = rundomizer.remove_fashionable_items(all_armor)
        for piece in filtered:
            self.assertTrue(piece.fashionable == 'False')
        self.assertTrue(len(filtered) < len(all_armor))


    
            


if __name__ == '__main__':
    unittest.main()
