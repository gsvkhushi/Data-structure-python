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

    def even(self):
       for i in range (0, len (self.stack),2):
          print(self.stack[i])  
    
if __name__=="__main__":
   s = stack()
   n=int(input("Enter the number of elements in stack:"))
   for i in range (n):
      s.push(int(input(f"Enter element {i+1}:")))

s.even()  