try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except:
    raise

import unittest
from calculator import sum

class TestCalculator(unittest.TestCase):
    def test_sum_5_5_10(self):
        self.assertEqual(
            sum(5,5),
            10,
        )
    
    def test_sum_5_5_12(self):
        self.assertEqual(
            sum(5,5),
            10,
        )
    
    def test_sum_multiple(self):
        x_y_output = (
            (5,5,10),
            (5,4,9),
            (-5,5,0),
            (2,2,4),
        )
        # for x,y,out in x_y_output:
        #     self.assertEqual(
        #         sum(x,y),
        #         out,
        #     )

        for item in x_y_output:
            with self.subTest(item=item):
                x,y,out = item
                self.assertEqual(
                    sum(x,y),
                    out,
                )
    
    def test_sum_parameters(self):
        with self.assertRaises(AssertionError):
            sum('11',9)

    
    
                

if __name__ == '__main__':
    unittest.main(verbosity=2)