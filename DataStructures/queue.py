class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self,value):
        self.items.append(value)
    
    def dequeue(self):
        if self.items:
            self.items.pop()

    def traverse(self):
        for item in self.items:
            print(item,end=" ")

q = Queue()
q.enqueue(4)
q.enqueue(4)
q.dequeue()
q.traverse()
