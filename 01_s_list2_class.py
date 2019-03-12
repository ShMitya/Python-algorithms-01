
# coding: utf-8

# In[126]:


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
    
    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
            
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        node_list = []
        while node is not None:
            if node.value == val:
                node_list.append(node)                
            node = node.next
        return node_list
    
    def delete (self, val, all=False):
        node = self.head
        if node is not None and node.value == val: 
            self.head = node.next
            if node.next is not None:
                node.next.prev = None 
            if node.next == None:
                self.tail = None
            if all == True:
                return self.delete(val, True)
            return
        
        while node is not None:
            if node.value == val:
                node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:#
                    self.tail = self.head
                    #node = None #
                    #return #
                if all == False:
                    return
            node = node.next
        pass
        
    def clean (self):
        self.head= None
        self.tail= None
        pass
        
    def len(self):
        node = self.head
        i = 0
        while node is not None:
            i+=1
            node=node.next
        return i
    
    def insert(self, afterNode, newNode):
        if afterNode == None:
            if self.head is None:
                self.head = newNode
                self.tail = self.head
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
            self.tail = newNode
            return
                        
        node = self.head
        while node is not None:
            if node.next is not None and node == afterNode: 
                newNode.next = node.next
                node.next.prev = newNode
                node.next = newNode
                newNode.prev = node
                if node.next.next == None:
                    self.tail = node.next
                return
            elif node.next == None:
                self.tail = newNode
                self.tail.prev = node
                node.next = self.tail
                return
            node = node.next
        pass
            
    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            newNode.prev = None
            newNode.next = None
            self.tail = self.head
        else:
            node = self.head
            self.head = newNode
            self.head.next = node
            node.prev = self.head #
        pass

