class HashTable:

    def __init__(self, table_size):           # can add additional attributes
        self.table_size = table_size          # initial table size
        self.hash_table = [None] * table_size # hash table
        self.num_items = 0                    # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        counter = 0
        orig_index = self.horner_hash(key)
        index = self.horner_hash(key)

        if not self.in_table(key):
            if self.hash_table[index] is None:
                self.hash_table[index] = (key, [])
                if value not in self.hash_table[index][1]:
                    self.hash_table[index][1].append(value)
            else:
                counter += 1
                index = self.probe(orig_index, counter)
                while self.hash_table[index] is not None and self.hash_table[index] != key and counter < self.table_size:
                    counter += 1
                    index = self.probe(orig_index, counter)
                if self.hash_table[index] is None:
                    self.hash_table[index] = (key, [])
                    if value not in self.hash_table[index][1]:
                        self.hash_table[index][1].append(value)
            self.num_items += 1
        else:
            index = self.get_index(key)
            if value not in self.hash_table[index][1]:
                self.hash_table[index][1].append(value)

        if self.get_load_factor() > 0.5:
            self.rehash()

    def rehash(self):
        tuplelist = []
        for i in self.hash_table:
            if i is not None:
                tuplelist.append(i)

        self.table_size = (self.table_size * 2) + 1
        self.hash_table = [None] * self.table_size
        self.num_items = 0

        for i in tuplelist:
            for j in i[1]:
                self.insert(i[0], j)

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        hash = 0

        if len(key) < 8:
            n = len(key)
        else:
            n = 8

        for i in range(n):
            hash += (ord(key[i]) * 31 ** (n - 1 - i))

        return hash % self.table_size

    def probe(self, orig_index, counter):
        return (orig_index + (counter ** 2)) % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        '''for i in self.hash_table:
            if i is not None:
                if i[0] == key:
                    return True
        return False'''
        orig_index = self.horner_hash(key)
        index = self.horner_hash(key)
        counter = 0
        found = False
        empty = False

        if self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return True
            else:
                while not found and not empty:
                    counter += 1
                    index = self.probe(orig_index, counter)
                    if self.hash_table[index] is None:
                        empty = True
                    elif self.hash_table[index][0] == key:
                        return True
        else:
            return False


    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        counter = 0
        found = False

        if self.in_table(key):
            orig_index = self.horner_hash(key)
            index = self.horner_hash(key)

            while self.hash_table[index] is not None and not found:
                if self.hash_table[index][0] == key:
                    found = True
                else:
                    counter += 1
                    index = self.probe(orig_index, counter)

            return index

        else:
            return None

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        alist = []

        for i in self.hash_table:
            if i is not None:
                alist.append(i[0])

        return alist

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        if self.in_table(key):
            index = self.get_index(key)
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
        else:
            return None

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

