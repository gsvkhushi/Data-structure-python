class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self, item):
       self.stack.append(item)
       print(f"pushed{item}")
       
    def pop(self):
       if self.is_empty():
          return "stack is empty!"
       print(f"popped:{self.stack.pop()}")

    def peek(self):
       if self.is_empty():
          return "stack is empty!"
       return f"top:{self.stack[-1]}"
    
    def is_empty(self):
       return len(self.stack)==0
    
    def size(self):
       return len(self.stack)
    
    def display(self):
       print ("stack(top -> bottom):", self.stack[::-1])
    
s =stack()
s.push(20)
print(s.peek())
s.push(30)
s.display()
print(s.pop())
print(s.peek())
s.display()    
            