## Stack implementation using Array
class Stack():

    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, val : int):

        self.top = self.top + 1
        self.arr[self.top] = val

    def pop(self):

        if( self.top == -1):
            print("Stack is Empty !!!")
        else:
            x = self.arr[self.top]
            self.top = self.top - 1
            return x

    def peek(self):
        x = self.arr[self.top]
        return x
    
    def display(self):
        for i in range(len(self.arr)):
            print(self.arr[i])