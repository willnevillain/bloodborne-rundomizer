import unittest
import rundomizer
from models import Weapon, Armor

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.armor = rundomizer.populate_armor()
        self.weapons = rundomizer.populate_weapons()

    def test_remove_plus_armor(self):
        filtered = rundomizer.remove_plus_items(self.armor)
        for piece in filtered:
            self.assertTrue(piece.location != 'NG+')
        self.assertTrue(len(filtered) < len(self.armor))
            
    def test_remove_plus_weapons(self):
        filtered = rundomizer.remove_plus_items(self.weapons)
        for weapon in filtered:
            self.assertTrue(weapon.location != 'NG+')
        self.assertTrue(len(filtered) < len(self.weapons))            

    def test_remove_chalice_armor(self):
        filtered = rundomizer.remove_chalice_items(self.armor)
        for piece in filtered:
            self.assertTrue(piece.location != 'Chalice')
        self.assertTrue(len(filtered) < len(self.armor))

    def test_remove_chalice_weapons(self):
        filtered = rundomizer.remove_chalice_items(self.weapons)
        for weapon in filtered:
            self.assertTrue(weapon.location != 'Chalice')
        self.assertTrue(len(filtered) < len(self.weapons))

    def test_remove_big_guns(self):
        filtered = rundomizer.remove_big_guns(self.weapons)
        for weapon in filtered:
            if weapon.slot == 'Firearm':
                self.assertTrue(weapon.requirements['str'] < 27)
        self.assertTrue(len(filtered) < len(self.weapons))
    
    def test_remove_fashionable_armor(self):
        filtered = rundomizer.remove_fashionable_items(self.armor)
        for piece in filtered:
            self.assertTrue(piece.fashionable == 'False')
        self.assertTrue(len(filtered) < len(self.armor))


if __name__ == '__main__':
    unittest.main()
