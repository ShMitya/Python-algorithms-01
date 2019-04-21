
# coding: utf-8

# In[1]:


class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        k = len(key)%self.size
        return k

    def is_key(self, key):
        k = self.hash_fun(key)
        
        if self.slots[k] is None:
            return False
        
        if key == self.slots[k]:
            return True
        elif key in self.slots[k]:
            return True
        return False

    def put(self, key, value):
        k = self.hash_fun (key)
        
        if self.slots[k] is None:
            self.slots[k] = key
            self.values[k] = value
            return
        
        if self.slots[k] == key:
            self.values[k] = value
            return
        
        if key in self.slots[k]:
            self.values[k][self.slots[k].index(key)] = value
            return           
            
        if type(self.slots[k]) == str:
            key_to_append = self.slots[k]
            value_to_append = self.values[k]
            self.slots[k] = []
            self.slots[k].append(key_to_append)
            self.slots[k].append(key)
            self.values[k] = []
            self.values[k].append(value_to_append)
            self.values[k].append(value)
                    
        elif type (self.slots[k]) == list:
            self.slots[k].append(key)
            self.values[k].append(value)

    def get(self, key):
        k = self.hash_fun(key)
        if self.is_key(key):
            if self.slots[k] == key:
                return self.values[k]
            return self.values[k][self.slots[k].index(key)]
        return None

