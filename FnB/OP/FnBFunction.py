#!/usr/bin/env python
# coding: utf-8

# In[14]:

class ZerroTransfer(Exception):
    pass



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
    try:
        if n > FnB_B.staffnum or n<0:
            raise(ZerroTransfer())
        else:
            FnB_A.staffnum += n
            FnB_B.staffnum -= n
            return True
    except ZerroTransfer:
        print("The number of staffs transferred is not valid")
    

