# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:39:52 2018

@author: User
"""

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

os.chdir('C:/Users/User/Pictures/Saved Pictures')


img1 = Image.open("suzy1.png")
img2 = Image.open("twice.jpg")

def img_processing(img):
    
    
        
    img_grayscale = img.convert("L")
    
    [n,m] = img.size
    U,S,V = np.linalg.svd(img_grayscale)
    B = np.zeros([m,n])
    
    min_mn =  min(m,n)
    
    
    for i in range(int(min_mn)):
        B = B + S[i] * np.outer(U[:,i],(V[i,:]))
        if (i+11) % 10 == 0:
            plt.title("i = %s" % str(i+1), loc="center" )
            plt.imshow(B, cmap='gray')
            plt.show()
        
img_processing(img1)
img_processing(img2)