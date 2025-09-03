class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"enqueued {item}")

    def dequeue(self):
        return(f"popped: {self.queue.pop()}")
    
    def size (self):
        return len(self.queue)
    
q = queue()
q.enqueue("ana")
q.enqueue("bob")
print(f"queue size :{q.size()}")

    
