## Queue implementation using the array
class Queue():

    def __init__(self):
        self.arr = []
        self.front = -1
        self.rear = -1

    def isEmpty(self):

        if(self.front == self.rear and not (self.front == 0)):
            return True
        return False
    
    def Enqueue(self,val):
        if(self.isEmpty()):
            self.front , self.rear = 0, 0
            self.arr[self.rear] = val
        else:
            self.rear = self.rear + 1
            self.arr[self.rear] = val
        

    def Dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty !!!")
        else:
            temp = self.arr[self.front]
            self.front = self.front + 1
            return temp
