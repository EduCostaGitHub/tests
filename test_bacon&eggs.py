import unittest
from bacon_with_eggs import bacon_with_eggs

"""
TDD - Test Driven Development

RED
Part 1 -> Make the Test e see the fail

GREEN
Part 2 -> Make the code and watch the test pass

REFACTOR
Part 3  -> Improve the code

"""

class TestBaconEggs(unittest.TestCase):

    def test_bacon_eggs_int_parameters(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('2')

    def test_bacon_eggs_output_if_multiple_of_3_and_5(self):
        inputs = (15,30,45,60)
        output = 'Bacon & eggs'

        for input in inputs:
            with self.subTest(input=input,output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f'{input} did not returned {output}'
                )

    def test_bacon_eggs_output_if__NOT_multiple_of_3_and_5(self):
        inputs = (1,2,4,7,8)
        output = 'starving'

        for input in inputs:
            with self.subTest(input=input,output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f'{input} did not returned {output}'
                )

    def test_bacon_eggs_output_if__multiple_of_3(self):
        inputs = (3, 12 , 21)
        output = 'Bacon'

        for input in inputs:
            with self.subTest(input=input,output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f'{input} did not returned {output}'
                )            
    def test_bacon_eggs_output_if__multiple_of_5(self):
        inputs = (5,10,20)
        output = 'eggs'

        for input in inputs:
            with self.subTest(input=input,output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f'{input} did not returned {output}'
                )            

unittest.main(verbosity=2)

