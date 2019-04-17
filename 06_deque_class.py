
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Deque:  
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addTail(self, item):
        item = Node (item)
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        
    def addFront(self, item):
        item = Node (item)
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
            self.tail = self.head
        else:
            node = self.head
            self.head = item
            self.head.next = node
            node.prev = self.head
    
    def removeFront(self):
        node_to_remove = self.head
        
        if self.head is not None:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None                
            else:
                self.tail = None
                self.head = None
            return node_to_remove.value
        else:
            return None
        
    def removeTail(self):
        node_to_remove = self.tail
        
        if self.tail is not None:
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.tail.next = None                
            else:
                self.tail = None
                self.head = None
            return node_to_remove.value
        else:
            return None
        
    def size(self):
        node = self.head
        i = 0
        while node is not None:
            i+=1
            node = node.next
        return i

