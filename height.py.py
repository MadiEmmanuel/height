#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('IMG_20171112_093350.jpg')
iar = np.asarray(i)

plt.imshow(iar)
plt.show()
    


# In[7]:


import sys
from PIL import Image
import numpy as np
j = Image.open('IMG_20180310_075056.jpg')
see = np.asarray(j)
print(see)


# In[ ]:




