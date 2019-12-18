import unittest
import day01

def input_data(file_name):
    try:
        with open(file_name) as file:
            data = file.read().split('\n')[:-1] # Remove trailing newline
            return data
    except FileNotFoundError as fnf_error:
        print(fnf_error)

class TestDay01(unittest.TestCase):

    def test_part01(self):
        self.assertEqual(day01.part01([12]), 2)
        self.assertEqual(day01.part01([14]), 2)
        self.assertEqual(day01.part01([1969]), 654)
        self.assertEqual(day01.part01([100756]), 33583)
        self.assertEqual(day01.part01(input_data('input/day01.in')), 3239890)

    def test_part02(self):
        self.assertEqual(day01.part02([14]), 2)
        self.assertEqual(day01.part02([1969]), 966)
        self.assertEqual(day01.part02([100756]), 50346)
        self.assertEqual(day01.part02(input_data('input/day01.in')), 4856963)

if __name__ == '__main__':
    unittest.main()
