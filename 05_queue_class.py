
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, value):
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
            
    def dequeue (self):
        node_to_pop = self.tail
        
        if self.tail is not None:
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.tail.next = None                
            else:
                self.tail = None
                self.head = None
            return node_to_pop.value
        else:
            return None

    def size (self):
        node = self.head
        i = 0
        while node is not None:
            i+=1
            node = node.next
        return i

