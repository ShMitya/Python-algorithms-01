
# coding: utf-8

# In[65]:


from bitarray import bitarray

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = bitarray(self.filter_len)
        self.filter.setall(False)


    def hash1(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result += result*17+code
        return result%self.filter_len

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result += result*223+code
        return result%self.filter_len
    
    def add(self, str1):
        str1_hash1 = bitarray(self.filter_len)
        str1_hash1.setall(False)
        str1_hash1[self.hash1(str1)] = True
        self.filter = self.filter | str1_hash1
        
        str1_hash2 = bitarray(self.filter_len)
        str1_hash2.setall(False)
        str1_hash2[self.hash2(str1)] = True
        self.filter = self.filter | str1_hash2
       
         

    def is_value(self, str1):
        str1_hash1 = self.hash1(str1)
        str1_hash2 = self.hash2(str1)
        return self.filter[str1_hash1] & self.filter[str1_hash1] 

