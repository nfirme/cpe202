from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root is None

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.root is None:
            return False
        return self.search_helper(key, self.root)

    def search_helper(self, key, node):
        if node is None:
            return False

        if key == node.key:
            return True
        elif key < node.key:
            return self.search_helper(key, node.left)
        elif key > node.key:
            return self.search_helper(key, node.right)

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            self.insert_helper(key, data, self.root)

    def insert_helper(self, key, data, node):
        if key < node.key:
            if node.left is None:
                new_node = TreeNode(key, data)
                node.left = new_node
            else:
                self.insert_helper(key, data, node.left)
        elif key > node.key:
            if node.right is None:
                new_node = TreeNode(key, data)
                node.right = new_node
            else:
                self.insert_helper(key, data, node.right)
        else:
            node.data = data

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        else:
            min_node = self.find_min_helper(self.root)
            min_tuple = (min_node.key, min_node.data)
            return min_tuple

    def find_min_helper(self, node):
        if node.left is None:
            return node
        else:
            return self.find_min_helper(node.left)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        else:
            max_node = self.find_max_helper(self.root)
            max_tuple = (max_node.key, max_node.data)
            return max_tuple

    def find_max_helper(self, node):
        if node.right is None:
            return node
        else:
            return self.find_max_helper(node.right)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.root is None:
            return None
        else:
            return self.height_helper(self.root)

    def height_helper(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height_helper(node.left), self.height_helper(node.right))

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        if self.root is None:
            return []
        else:
            return self.inorder_helper(self.root)

    def inorder_helper(self, node):
        res = []
        if node is not None:
            res = self.inorder_helper(node.left)
            res.append(node.key)
            res = res + self.inorder_helper(node.right)
        return res

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.root is None:
            return []
        else:
            return self.preorder_helper(self.root)

    def preorder_helper(self, node):
        res = []
        if node is not None:
            res.append(node.key)
            res = res + self.preorder_helper(node.left)
            res = res + self.preorder_helper(node.right)
        return res

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        if self.root is None:
            return []

        lev_list = []
        q = Queue(25000)  # Don't change this!

        q.enqueue(self.root)

        while not q.is_empty():
            cur = q.dequeue()
            lev_list.append(cur.key)
            if cur.left is not None:
                q.enqueue(cur.left)
            if cur.right is not None:
                q.enqueue(cur.right)

        return lev_list






        

