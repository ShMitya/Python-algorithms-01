
# coding: utf-8

# In[2]:


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 > v2:
            if self.__ascending == True:
                return 1
            if self.__ascending == False:
                return -1
        elif v1 < v2:
            if self.__ascending == True:
                return -1
            if self.__ascending == False:
                return 1
        elif v1 == v2:
            return 0

    def add(self, value):
        newNode = Node(value)
        
        if self.head is None:
            self.head = newNode
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
            return
        
        node = self.head
        while node is not None:
            if self.compare (value, node.value) == -1:
                self.head = newNode
                newNode.next = node
                node.prev = newNode
                newNode.prev = None
                return
            
            elif self.compare (value, node.value) == 0:
                newNode.prev = node.prev
                node.prev = newNode
                newNode.next = node
                if newNode.prev is not None:
                    newNode.prev.next = newNode
                else:
                    self.head = newNode
                return
            
            elif self.compare (value, node.value) == 1 and node.next is not None and self.compare (value, node.next.value)== -1:
                newNode.next = node.next
                node.next = newNode
                newNode.prev = node
                newNode.next.prev = newNode
                return
                
            elif self.compare (value, node.value) == 1 and node.next is None:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                return
            
            node = node.next
            
        
    def find(self, val):
        if self.head is None:
            return None
        
        if self.__ascending == True:
            node = self.head
            while node is not None and node.value <= val:
                if node.value == val:
                    return node
                node = node.next
        elif self.__ascending == False:
            node = self.tail
            while node is not None and node.value <= val:
                if node.value == val:
                    return node
                node = node.prev
        return None
                
    def delete(self, val):
        node = self.head
        if node is not None and node.value == val: 
            self.head = node.next
            if node.next is not None:
                self.head.prev = None
            if node.next == None:
                self.tail = None
            return
        
        while node is not None:
            if node.value == val:
                node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                    self.tail.next = None
                return
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head= None
        self.tail= None

    def len(self):
        node = self.head
        i = 0
        while node is not None:
            i+=1
            node=node.next
        return i

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        s1 = v1.strip().lower()
        s2 = v2.strip().lower()
        if min(s1, s2)== s2: 
            if self.__ascending == True:
                return 1
            if self.__ascending == False:
                return -1
        elif min(s1, s2)== s1:
            if self.__ascending == True:
                return -1
            if self.__ascending == False:
                return 1
        elif s1 == s2:
            return 0

