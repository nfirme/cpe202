import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

    def test_base17(self):
        with self.assertRaises(ValueError):
            convert(1024, 17)

    def test_num0(self):
        self.assertEqual(convert(0, 2), "0")

if __name__ == "__main__":
        unittest.main()