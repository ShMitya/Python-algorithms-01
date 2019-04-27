
# coding: utf-8

# In[65]:


class PowerSet:

    def __init__(self):
        self.set_size = 49999
        self.step = 3
        self.slots = [None]*self.set_size
        
    def size(self):
        sz = 0
        for i in self.slots:
            if i is not None:
                sz += 1
        return sz
    
    def hash_fun(self, value):
        if type(value) == str:
            result = 0
            for c in value:
                result += result+ord(c)
        else:
            result = value
            
        k = int(result % self.set_size)
        return k
    
    def seek_slot(self, value):
        k = self.hash_fun(value)
        k_initial = k
        while self.slots[k] is not None:
            k = (k + self.step)%self.set_size
            if k == k_initial:
                return None
        return k
        

    def put(self, value):
        if self.get(value) == False:
            k = self.seek_slot(value)
            if k is not None:
                self.slots[k] = value

    def get(self, value):
        if value in self.slots:
            return True
        return False

    def remove(self, value):
        k = self.hash_fun(value)
        if self.get(value):
            while self.slots[k] != value:
                k += self.step
            self.slots[k] = None
            return True
        return False

    def intersection(self, set2):
        set_to_return = PowerSet()
        started = True
        for i in self.slots:
            if i is not None and set2.get(i):
                set_to_return.put(i)
        return set_to_return  

    def union(self, set2):
        set_to_return = set2
                
        if self.size() == 0:
            return set_to_return
            
        for i in self.slots:
            if i is not None and set2.get(i) == False:
                set_to_return.put(i)
        return set_to_return  

    def difference(self, set2):
        set_to_return = self
        for i in self.slots:
            if i is not None and set2.get(i):
                set_to_return.remove(i)   
        return set_to_return

    def issubset(self, set2):
        for i in set2.slots:
            if i is not None and self.get(i) == False:
                return False
        return True

