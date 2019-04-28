
# coding: utf-8

# In[70]:


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
                k = (k + self.step)%self.set_size
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
        set_to_return = PowerSet()
        set_to_return.slots = set2.slots.copy()
                
        if self.size() == 0:
            return set_to_return
            
        for i in self.slots:
            if i is not None and set2.get(i) == False:
                set_to_return.put(i)
        return set_to_return    

    def difference(self, set2):
        set_to_return = PowerSet()
        set_to_return.slots = self.slots.copy()
        for i in self.slots:
            if i is not None and set2.get(i):
                set_to_return.remove(i)   
        return set_to_return

    def issubset(self, set2):
        for i in set2.slots:
            if i is not None and self.get(i) == False:
                return False
        return True


# In[71]:


print ('Тест put добавляется')
ps_to_test = PowerSet()
ps_to_test.put(12)
ps_to_test.put(12.1)
ps_to_test.put(12.2)
ps_to_test.put(12.3)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_to_test.put('123')
ps_to_test.put(123)
ps_to_test.put('666')
ps_to_test.put(657)
ps_to_test.put('666')
ps_to_test.put(True)
ps_to_test.put(True)
ps_to_test.put(False)
ps_to_test.put(False)
ps_to_test.put(0)
ps_to_test.put(1)
print ('Размер множества после трех разных добавлений:', ps_to_test.size())


# In[72]:


for i in ps_to_test.slots:
    if i is not None:
        print(i)


# In[73]:


print ('Тест put не добавляется')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
print ('Размер множества после трех разных и трех повторных добавлений:', ps_to_test.size())


# In[74]:


print ('Тест remove элемент есть и удален')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
print ('Удаление элемента:', ps_to_test.remove(12.3))
print ('Размер множества должен быть 2:', ps_to_test.size(), 'Попытка get удаленного элемента', ps_to_test.get(12.3))


# In[75]:


print ('Тест remove элемента нет')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
print ('Удаление элемента:', ps_to_test.remove(666))
print ('Размер множества должен быть 3:', ps_to_test.size(), 'Попытка get удаленного элемента', ps_to_test.get(666))


# In[76]:


print ('Тест intersection - на выходе пустое множество')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_in = PowerSet()
ps_in.put('sdgfhgh')
ps_in.put(243454.23)
ps_in.put(228)
ps_out = ps_to_test.intersection(ps_in)
print ('На выходе множество размера 0:', ps_out.size() == 0)


# In[77]:


print ('Тест intersection - на выходе НЕпустое множество')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_in = PowerSet()
ps_in.put('sdgfhgh')
ps_in.put('123')
ps_in.put(123)
ps_out = ps_to_test.intersection(ps_in)
print ('На выходе размер на выходе 2:', ps_out.size(), 'Наличие элементов 123 и _123_:', ps_out.get(123), ps_out.get('123'))


# In[78]:


print ('Тест union - оба множества НЕпустые')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_in = PowerSet()
ps_in.put('sdgfhgh')
ps_in.put('123')
ps_in.put(123)
ps_out = ps_to_test.union(ps_in)
print ('На выходе размер на выходе 4:', ps_out.size(), 'Наличие элементов 12.3 и _sdgfhgh_:', ps_out.get(12.3), ps_out.get('sdgfhgh'))


# In[79]:


print ('Тест union - второе множество - пустое')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_in = PowerSet()
ps_out = ps_to_test.union(ps_in)
print ('На выходе размер на выходе 3:', ps_out.size())


# In[80]:


print ('Тест union - первое множество пустое')
ps_to_test = PowerSet()
ps_in = PowerSet()
ps_in.put('sdgfhgh')
ps_in.put('123')
ps_in.put(123)
ps_out = ps_to_test.union(ps_in)
print ('На выходе размер на выходе 3:', ps_out.size())


# In[81]:


print ('Тест union - оба множества пустые')
ps_to_test = PowerSet()
ps_in = PowerSet()
ps_out = ps_to_test.union(ps_in)
print ('На выходе множество размера 0:', ps_out.size() == 0)


# In[82]:


print ('Тест difference - на выходе НЕпустое множество')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_in = PowerSet()
ps_in.put('sdgfhgh')
ps_in.put('123')
ps_in.put(123)
ps_in.put(83292)
ps_out = ps_to_test.difference(ps_in)
print ('На выходе размер на выходе 1:', ps_out.size(), 'Наличие элементов 12.3:', ps_out.get(12.3))


# In[83]:


print ('Тест difference - на выходе пустое множество')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_in = PowerSet()
ps_in.put(12.3)
ps_in.put('123')
ps_in.put(123)
ps_out = ps_to_test.difference(ps_in)
print ('На выходе множество размера 0:', ps_out.size() == 0)


# In[84]:


print ('Тест issubset - все элементы параметра входят в текущее множество')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_to_test.put('sdgfgn')
ps_to_test.put(666)
ps_to_test.put(412)
ps_in = PowerSet()
ps_in.put(12.3)
ps_in.put('123')
ps_in.put(123)
ps_out = ps_to_test.issubset(ps_in)
print ('На выходе True:', ps_out)


# In[85]:


print ('Тест issubset - все элементы текущего множества входят в параметр')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_to_test.put('sdgfgn')
ps_to_test.put(666)
ps_to_test.put(412)
ps_in = PowerSet()
ps_in.put(12.3)
ps_in.put('123')
ps_in.put(123)
ps_out = ps_in.issubset(ps_to_test)
print ('На выходе False:', ps_out)


# In[86]:


print ('Тест issubset - не все элементы параметра входят в текущее множество')
ps_to_test = PowerSet()
ps_to_test.put(123)
ps_to_test.put(12.3)
ps_to_test.put('123')
ps_to_test.put('sdgfgn')
ps_to_test.put(666)
ps_to_test.put(412)
ps_in = PowerSet()
ps_in.put(12.3)
ps_in.put('123')
ps_in.put(123)
ps_in.put('AAAAA')
ps_out = ps_to_test.issubset(ps_in)
print ('На выходе False:', ps_out)


# In[87]:


ps_to_test = PowerSet()
for i in range (11000):
    ps_to_test.put(10**i)
ps_to_test.size()


# In[88]:


ps_to_test2 = PowerSet()
for i in range (11000):
    ps_to_test2.put(3**i)
ps_to_test2.size()


# In[89]:


ps_out = ps_to_test.union(ps_to_test2)
ps_out.size()


# In[90]:


ps_to_test.size()


# In[91]:


ps_to_test2.size()

