#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
from TestHRFunction import Test_HRFunction
from TestStaffClass import Test_StaffClass
from TestFnBFunction import Test_FnBFunction
from TestFnBClass import Test_FnBClass

def my_suite():
    suite  = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(Test_HRFunction))
    suite.addTest(unittest.makeSuite(Test_StaffClass))
    suite.addTest(unittest.makeSuite(Test_FnBClass))
    suite.addTest(unittest.makeSuite(Test_FnBFunction))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
my_suite()


# In[ ]:




