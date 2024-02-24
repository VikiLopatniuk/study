import unittest
import man_func


class PositiveTests(unittest.TestCase):

    def test_man_1(self):
        persons = {
            'person1': {'gender': 'Male', 'height': 175},
            'person2': {'gender': 'Female', 'height': 160},
            'person3': {'gender': 'Male', 'height': 180},
            'person4': {'gender': 'Male', 'height': 130},
            'person5': {'gender': 'Male', 'height': 200},
            'person6': {'gender': 'Female', 'height': 210},
            'person7': {'gender': 'Female', 'height': 110},
            'person8': {'gender': 'Male', 'height': 120},
            'person9': {'gender': 'Male', 'height': 140},
            'person10': {'gender': 'Male', 'height': 150},
        }
        expected = (175 + 180 + 130 + 200 + 120 + 140 + 150) / 7
        actual_result = man_func.man_height(persons)
        self.assertEqual(expected, actual_result)

    def test_man_2(self):
        persons = {
            'person1': {'gender': 'Female', 'height': 175},
            'person2': {'gender': 'Female', 'height': 160},
            'person3': {'gender': 'Female', 'height': 180},
            'person4': {'gender': 'Male', 'height': 110},
            'person5': {'gender': 'Male', 'height': 230},
            'person6': {'gender': 'Female', 'height': 270},
            'person7': {'gender': 'Female', 'height': 120},
            'person8': {'gender': 'Male', 'height': 110},
            'person9': {'gender': 'Male', 'height': 140},
            'person10': {'gender': 'Male', 'height': 150},
        }
        expected = (110 + 230 + 110 + 140 + 150) / 5
        actual_result = man_func.man_height(persons)
        self.assertEqual(expected, actual_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
