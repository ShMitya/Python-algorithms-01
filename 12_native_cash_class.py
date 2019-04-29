
# coding: utf-8

# In[3]:


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.step = 3
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        result = 0
        for c in key:
            code = ord(c)
            result += result*17+code
        return result%self.size
    
    def is_key(self, key):
        k = self.hash_fun(key)
        i = 0
        while self.slots[k] != None and i != self.size:
            if self.slots[k] == key:
                return True
            k = (k + self.step)%self.size
            i += 1
        return False

    def seek_slot(self, key):
        k = self.hash_fun(key)
        i = 0
        while self.slots[k] is not None and self.slots[k] != key:
            k = (k + self.step)%self.size
            i += 1
            if i == self.size:
                return None
        return k
    
    def put(self, key, value):
        k = self.seek_slot(key)
        
        if k is not None:
            self.slots[k] = key
            self.values[k] = value
            self.hits[k] = 1
        
        else:
            k_to_pull = self.hits.index(min(self.hits)) 
            self.slots[k_to_pull] = key
            self.values[k_to_pull] = value
            self.hits[k_to_pull] = 1

    def get(self, key):
        k = self.seek_slot(key)
        if k is not None:
            self.hits[k] += 1
            return self.values[k]
        return None

