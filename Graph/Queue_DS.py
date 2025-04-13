## Queue implementation using the array
class Queue():

    def __init__(self):
        self.front = -1
        self.rear = -1
        self.arr = []

    def isEmpty(self):
        if( self.front == -1 or self.front > self.rear):
            return True
        else:
            return False
    
    def enqueue( self, val):
        if(self.isEmpty()):
            self.front = 0
            self.rear = 0
        else:
            self.rear = self.rear + 1
        self.arr.insert(self.rear,val)

    def dequeue(self):
        if( self.isEmpty()):
            print("Empty Array !!!")
        else:
            temp = self.arr.pop(self.front)
            self.rear = self.rear - 1
            return temp
    
    def display(self):
        x = self.front
        while( x <= self.rear):
            print(self.arr[x])

            x = x + 1

if __name__ == "__main__":

    q = Queue()

    print(q.isEmpty())

    q.enqueue(12)
    q.enqueue(1)
    q.enqueue(15)
    q.enqueue(19)

    q.display()

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
        
