
# coding: utf-8

# In[2]:


import numpy

ref = 2.12

def height(h):
    
    if h > ref: 
        result = ref - h 
        result = abs(result)
    
    else:
        result = ref - h
        
    
    return result

height(3)
    

