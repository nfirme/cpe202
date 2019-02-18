import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_create_code2(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '11')
        self.assertEqual(codes[ord('b')], '01')
        self.assertEqual(codes[ord('c')], '101')
        self.assertEqual(codes[ord('d')], '100')
        self.assertEqual(codes[ord(' ')], '00')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_03_mutliline_file(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04_declaration(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_05_textfile(self):
        freqlist = cnt_freq("file3.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)
        self.assertEqual(freqlist[10], 1)

    def test_06_single_char(self):
        huffman_encode("single.txt", "single_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_07_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode("invisiblefile.txt", "invisiblefile_out.txt")

    def test_08_empty(self):
        huffman_encode("empty.txt", "empty_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_09_beemovie(self):
        huffman_encode("beemovie.txt", "beemovie_out.txt")
        err = subprocess.call("diff -wb beemovie_out.txt beemovie_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_01(self):
        huffman_encode("file1.txt", "file1_out.txt")
        huffman_decode("file1_out.txt", "file1_decomp.txt")
        err = subprocess.call("diff -wb file1.txt file1_decomp.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_02(self):
        huffman_encode("file2.txt", "file2_out.txt")
        huffman_decode("file2_out.txt", "file2_decomp.txt")
        err = subprocess.call("diff -wb file2.txt file2_decomp.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_03(self):
        huffman_encode("file3.txt", "file3_out.txt")
        huffman_decode("file3_out.txt", "file3_decomp.txt")
        err = subprocess.call("diff -wb file3.txt file3_decomp.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_multi(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        huffman_decode("multiline_out.txt", "multiline_decomp.txt")
        err = subprocess.call("diff -wb multiline.txt multiline_decomp.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_single(self):
        huffman_encode("single.txt", "single_out.txt")
        huffman_decode("single_out.txt", "single_decomp.txt")
        err = subprocess.call("diff -wb single.txt single_decomp.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_declaration(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        huffman_decode("declaration_out.txt", "declaration_decomp.txt")
        err = subprocess.call("diff -wb declaration.txt declaration_decomp.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_empty(self):
        huffman_encode("empty.txt", "empty_out.txt")
        huffman_decode("empty_out.txt", "empty_decomp.txt")
        err = subprocess.call("diff -wb empty.txt empty_decomp.txt", shell = True)
        self.assertEqual(err, 0)

    """def test_wap(self):
        huffman_encode("wap.txt", "wap_out.txt")
        huffman_decode("wap_out.txt", "wap_decomp.txt")
        err = subprocess.call("diff -wb wap.txt wap_decomp.txt", shell = True)
        self.assertEqual(err, 0)"""


if __name__ == '__main__': 
   unittest.main()
