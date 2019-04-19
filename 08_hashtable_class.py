
# coding: utf-8

# In[1]:


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        k = len(value)%self.size
        return k

    def seek_slot(self, value):
        k = self.hash_fun(value)
        for i in range (self.size):
            if self.slots[k] is None:
                return k
            k = (k + self.step)%self.size 
        return None
    
    def put(self, value):
        k = self.seek_slot(value)
        if k is not None:
            self.slots[k] = value
            return k
        return None

    def find(self, value):
        k = self.hash_fun(value)
        for i in range (self.size):
            if self.slots[k] == value:
                return k
            k = (k + self.step)%self.size
        return None

