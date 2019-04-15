
# coding: utf-8

# In[1]:


# Стек, работающий с головы

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def size (self):
        node = self.head
        i = 0
        while node is not None:
            i+=1
            node = node.next
        return i
    
    def push(self, value):
        newNode = Node (value)
        
        if self.head is None:
            self.head = newNode
            newNode.prev = None
            newNode.next = None
            self.tail = self.head
        else:
            node = self.head
            self.head = newNode
            self.head.next = node
            node.prev = self.head 
          
    def pop (self):
        node_to_pop = self.head
        
        if self.head is not None:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None                
            else:
                self.tail = None
                self.head = None
            return node_to_pop.value
        else:
            return None
                    
    def peek (self):
        if self.head is not None:
            return self.head.value
        else:
            return None

