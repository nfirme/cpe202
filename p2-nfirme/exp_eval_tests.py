# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_invalid_operator(self):
        try:
            postfix_eval("3 2 ^")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_illegal_bitshift_input(self):
        try:
            postfix_eval("3 2.0 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_illegal_bitshift_intermediate(self):
        try:
            postfix_eval("3 2 / 2 ** 4 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_illegal_bitshift_left(self):
        try:
            postfix_eval("3 2.0 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_bitshift_left(self):
        self.assertAlmostEqual(postfix_eval("3 5 * 10 <<"), 15360)

    def test_postfix_eval_bitshift_right(self):
        self.assertAlmostEqual(postfix_eval("3 5 * 10 >>"), 0)

    def test_postfix_eval_divide_by_0_input(self):
        with self.assertRaises(ValueError):
            postfix_eval("10 0 /")

    def test_postfix_eval_divide_by_0_intermediate(self):
        with self.assertRaises(ValueError):
            postfix_eval("100 10 10 - /")

    def test_postfix_eval_space_varied(self):
        self.assertAlmostEqual(postfix_eval("3     2 5   * 7   /  +"), 4.42857142857)

    def test_postfix_eval_floats(self):
        self.assertAlmostEqual(postfix_eval("4.1 2.8 * 4.4 9.0 / -"), 10.9911111111)

    def test_postfix_eval_floats_and_ints(self):
        self.assertAlmostEqual(postfix_eval("4.1 3 * 4.4 9 / -"), 11.8111111111)

    def test_postfix_eval_negative(self):
        self.assertAlmostEqual(postfix_eval("4 -2 * -3 -"), -5)

    def test_postfix_eval_exponents(self):
        self.assertAlmostEqual(postfix_eval("4 3 2 ** *"), 36)

    def test_postfix_eval_negative_exponents(self):
        self.assertAlmostEqual(postfix_eval('3 -2 ** 2 *'), 0.222222222222)

    def test_postfix_eval_empty_string(self):
        self.assertEqual(postfix_eval('    '), 0)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("6 - 3 * 2"), "6 3 2 * -")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_float(self):
        self.assertEqual(infix_to_postfix("6 - 3 + 2.0 * 5.5"), "6 3 - 2.0 5.5 * +")

    def test_infix_to_postfix_bitshift_right(self):
        self.assertAlmostEqual(infix_to_postfix("6 - 3 >> 2"), "6 3 2 >> -")

    def test_infix_to_postfix_bitshift_left(self):
        self.assertAlmostEqual(infix_to_postfix("6 - 3 << 2"), "6 3 2 << -")

    def test_infix_to_postfix_empty_string(self):
        self.assertEqual(infix_to_postfix(""), "")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_single(self):
        self.assertEqual(prefix_to_postfix('6'), '6')

    def test_prefix_to_postfix_exponents(self):
        self.assertEqual(prefix_to_postfix('- * 3 2 ** 10 4'), '3 2 * 10 4 ** -')

    def test_prefix_to_postfix_empty_string(self):
        self.assertEqual(prefix_to_postfix(""), "")






if __name__ == "__main__":
    unittest.main()
