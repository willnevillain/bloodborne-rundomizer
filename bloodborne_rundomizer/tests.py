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
    
    def test_remove_torches(self):
        torches = ['Torch', "Hunter's Torch"]
        filtered = rundomizer.remove_torches(self.weapons)
        for weapon in filtered:
            self.assertTrue(weapon.name not in torches)
        self.assertTrue(len(filtered) < len(self.weapons))

    def test_remove_shields(self):
        shields = ['Wooden Shield', 'Loch Shield']
        filtered = rundomizer.remove_shields(self.weapons)
        for weapon in filtered:
            self.assertTrue(weapon.name not in shields)
        self.assertTrue(len(filtered) < len(self.weapons))


if __name__ == '__main__':
    unittest.main()
