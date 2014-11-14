__author__ = 'nathan'
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.prev = None

class BinaryTree:
    root = None
    def last(self, node = None):
        if(not node):
            node = self.root
        if(not node.next)
            return node
        else:
            return self.last(node.next)

    def insert(self, obj):
        if (not self.root):
            self.root = Node(obj)
        else:
            self.last().next = Node(obj)
alphabet = BinaryTree()
alphabet.insert('l')

