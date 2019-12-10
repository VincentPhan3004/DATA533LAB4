#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as plt



def compare(FnB_A,FnB_B): #show a bar plot with the revenues of FnB business
    try:
        profitrateA = FnB_A.revenue/FnB_A.area
        profitrateB = FnB_B.revenue/FnB_B.area
        if profitrateA >= profitrateB:
            return FnB_A
        else:
            return FnB_B
    except ZeroDivisonError:
        print(" One of the restaurants has zero area")
    
def staffTransfer(FnB_A,FnB_B,n): #transfer n staffs from group B to group A
    if n > FnB_B.staffnum or n<0:
        print("Can not implement the process")
        return False
    else:
       FnB_A.staffnum += n
       FnB_B.staffnum -= n
       return True

    

