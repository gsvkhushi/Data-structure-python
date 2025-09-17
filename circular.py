class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            # Traverse to the last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    
    def display(self):
        elements = []
        if not self.head:
            return elements
        temp = self.head
        while True:
            elements.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return elements


cll = CircularLinkedList()

cll.insert_end(10)
cll.insert_end(20)
cll.insert_beginning(5)
cll.insert_beginning(1)


print("Circular Linked List:", cll.display())
