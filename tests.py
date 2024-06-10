#def convert_cel_to_far(C=0.0):
#    F_temperature = C * 9/5 + 32
#    F_statement = f"{C:.0f} degrees C = {F_temperature:.2f} degrees F"
#    print(F_statement)

#convert_cel_to_far()

import unittest
from pets import multiply

class Multiply_test(unittest.TestCase):
    """Tests For Multiply Function"""

    def test_multiply(self):
        """Does String And Integer Multiply?"""
        num = multiply(2, "3")
        self.assertEqual(num, "333")

import sys

sys.exit()