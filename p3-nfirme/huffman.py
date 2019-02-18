import os

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the frequency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def __lt__(self, other):
        return comes_before(self, other)

    """def __repr__(self):
        return "Char: %s Freq: %s" % (self.char, self.freq)"""


def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq != b.freq:
        return a.freq < b.freq
    else:
        return a.char < b.char


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    if a.char < b.char:
        min = a.char
    else:
        min = b.char
    new_node = HuffmanNode(min, a.freq + b.freq)
    new_node.set_left(a)
    new_node.set_right(b)
    return new_node


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    freq_list = [0] * 256
    file = open(filename, "r")
    f = file.read()
    for c in f:
        freq_list[ord(c)] += 1
    file.close()

    return freq_list


def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    node_list = []

    for index, i in enumerate(char_freq):
        if i != 0:
            node = HuffmanNode(index, i)
            node_list.append(node)

    if len(node_list) == 1:
        return None

    node_list.sort()

    while len(node_list) > 1:
        node1 = node_list.pop(0)
        node2 = node_list.pop(0)
        new_node = combine(node1, node2)
        node_list.append(new_node)
        node_list.sort()

    node_list.append(new_node)

    return node_list[0]


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    code_list = [""] * 256
    code = ""

    return code_helper(node, code, code_list)


def code_helper(node, code, list):
    if node is None:
        return []
    if node.left is None and node.right is None:
        list[node.char] = code
        return list
    if node.left is not None:
        code_helper(node.left, code + "0", list)
    if node.right is not None:
        code_helper(node.right, code + "1", list)
    return list


def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list associated with "aaabbbbcc, would return “97 3 98 4 99 2” """
    header = ""
    for index, i in enumerate(freqs):
        if i != 0:
            header = header + str(index) + " " + str(i) + " "
    return header.rstrip()


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    try:
        file = open(in_file, "r")
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    if os.stat(in_file).st_size == 0:
        output = open(out_file, "w+")
    else:
        freq_list = cnt_freq(in_file)
        root = create_huff_tree(freq_list)
        code_list = create_code(root)
        header = create_header(freq_list)

        output = open(out_file, "w+")
        output.write(header)
        if code_list:
            output.write("\n")
            with open(in_file) as input:
                for line in input:
                    for ch in line:
                        output.write(code_list[ord(ch)])
        else:
            pass

    output.close()

def huffman_decode(encoded_file, decode_file):
    output = open(decode_file, "w+")

    # checks for empty encoded_file, closes decode_file without writing
    if os.stat(encoded_file).st_size == 0:
        output.close()
        return

    # gets header from encoded_file, saves as string
    with open(encoded_file) as f:
        header_string = f.readline().strip()

    # creates list of char freqs from header string, used to create huff tree
    list_of_freqs = parse_header(header_string)
    node = root = create_huff_tree(list_of_freqs)

    # special case: single character
    count = 0
    for i in list_of_freqs:
        if i != 0:
            count += 1

    if count == 1:
        single_list = header_string.split()
        char = chr(int(single_list[0]))
        freq = int(single_list[1])

        for i in range(freq):
            output.write(char)

        output.close()
        return

    with open(encoded_file) as file:
        file.readline()
        for line in file:
            for digit in line:

                if digit == '0':
                    node = node.left
                elif digit == '1':
                    node = node.right

                if node.left is None and node.right is None:
                    output.write(chr(node.char))
                    node = root
    output.close()

def parse_header(header_string):
    header_list = header_string.split()

    freqs = [0] * 256

    for index, j in enumerate(header_list):
        if index % 2 == 0:
            freqs[int(j)] = int(header_list[index + 1])

    return freqs




