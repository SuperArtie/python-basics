__author__ = 'nathan'

class Stack:
    data = []
    def push(self, name):
        self.data.append(name)
    def pop(self):
        self.data.pop()

food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')
food.pop()
pass