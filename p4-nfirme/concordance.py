from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            file = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError

        for line in file:
            line = line.strip()
            self.stop_table.insert(line, 0)

        file.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        num = 0
        try:
            file = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError

        for line in file:
            num += 1
            line = line.strip()
            line = line.lower()
            line = line.replace("'", "")
            emit = string.punctuation + "0123456789-"
            translator = str.maketrans(emit, ' ' * len(emit))
            line = line.translate(translator)
            line = line.split()

            for word in line:
                if not self.stop_table.in_table(word):
                    self.concordance_table.insert(word, num)

        file.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        file = open(filename, "w")
        word_list = self.concordance_table.get_all_keys()
        word_list.sort()
        alist = []
        for word in word_list:
            output = "" + word + ": "
            val_list = self.concordance_table.get_value(word)
            output += " ".join(map(str, val_list))
            alist.append(output)

        file.write("\n".join(alist))
        file.close()
