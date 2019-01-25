
# coding: utf-8

# In[2]:


import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('IMG_20171112_093350.jpg')
iar = np.asarray(i)

plt.imshow(iar)
plt.show()
    

