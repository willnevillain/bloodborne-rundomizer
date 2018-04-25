import unittest
import rundomizer
from models import Weapon, Armor

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.armor = rundomizer.populate_armor()
        self.weapons = rundomizer.populate_weapons()

    def test_remove_chalice_equipment(self):
        filtered_lists = [rundomizer.remove_chalice_items(self.armor), rundomizer.remove_chalice_items(self.weapons)]
        for filtered_list in filtered_lists:
            for equipment in filtered_list:
                self.assertTrue(equipment.chalice != 'True')
        self.assertTrue((len(filtered_lists[0]) < len(self.armor)) and (len(filtered_lists[1]) < len(self.weapons)))

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
