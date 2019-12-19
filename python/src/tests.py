import unittest
import day01, day02, day03

def input_data(file_name, sep, type='string'):
    try:
        with open(file_name) as file:
            data = file.read().split(sep)[:-1] # Remove trailing newline
            if type == 'int':
                data = [int(d) for d in data]
            return data
    except FileNotFoundError as fnf_error:
        print(fnf_error)

class TestDay01(unittest.TestCase):

    def test_part01(self):
        self.assertEqual(day01.part01([12]), 2)
        self.assertEqual(day01.part01([14]), 2)
        self.assertEqual(day01.part01([1969]), 654)
        self.assertEqual(day01.part01([100756]), 33583)
        self.assertEqual(day01.part01(input_data('input/day01.in', '\n')), 3239890)

    def test_part02(self):
        self.assertEqual(day01.part02([14]), 2)
        self.assertEqual(day01.part02([1969]), 966)
        self.assertEqual(day01.part02([100756]), 50346)
        self.assertEqual(day01.part02(input_data('input/day01.in', '\n')), 4856963)

class TestDay02(unittest.TestCase):

    def test_part01(self):
        self.assertEqual(day02.part01([1,0,0,0,99]), [2,0,0,0,99])
        self.assertEqual(day02.part01([2,3,0,3,99]), [2,3,0,6,99])
        self.assertEqual(day02.part01([2,4,4,5,99,0]), [2,4,4,5,99,9801])
        self.assertEqual(day02.part01([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])
        test_data = input_data('input/day02.in', ',', 'int')
        test_data[1] = 12
        test_data[2] = 2
        self.assertEqual(day02.part01(test_data)[0], 2692315)

    def test_part02(self):
        test_data = input_data('input/day02.in', ',', 'int')
        self.assertEqual(day02.part02(test_data), 9507)

class TestDay03(unittest.TestCase):

    def test_part01(self):
        wire1_1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
        wire1_2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
        wire2_1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
        wire2_2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
        self.assertEqual(day03.part01(wire1_1, wire1_2), 159)
        self.assertEqual(day03.part01(wire2_1, wire2_2), 135)
        test_data = input_data('input/day03.in', '\n')
        test_data_wire1 = test_data[0].split(',')
        test_data_wire2 = test_data[1].split(',')
        self.assertEqual(day03.part01(test_data_wire1, test_data_wire2), 489)

    # def test_part02(self):
    #     test_data = input_data('input/day02.in', ',', 'int')
    #     self.assertEqual(day02.part02(test_data), 9507)

if __name__ == '__main__':
    unittest.main()
