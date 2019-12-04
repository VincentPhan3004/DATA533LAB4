#!/usr/bin/env python
# coding: utf-8

# In[5]:


import unittest 
from FnB.OP.FnBClass import *

class Test_FnBClass(unittest.TestCase): # test class
    @classmethod
    def setUpClass(cls):
        print("Beginning FnBClass Testing")  
    
    @classmethod
    def tearDownClass(self):
        print("Ending FnBClass Testing")
        
    def setUp(self): 
        print('Begin a test case in Test_FnBClass')
        self.p1 = FnB("145 Ponto road", 145, 135000, 10)
        self.p2 = DeliveryFnB("129 King street", 25, 85000, 3,"UberEat")
        
    def tearDown(self):
        print('Finish a test case in Test_FnBClass')
    
    def test_FnB(self): # test case
        self.assertEqual(self.p1.address,"145 Ponto road")
        self.assertNotEqual(self.p1.area,146)
        self.assertIsNot(self.p1.staffnum,11)
        self.assertIsNotNone(self.p1.revenue)
        self.assertIsInstance(self.p1, FnB)
        
    def test_DeliveryFnB(self): # test case
        self.assertEqual(self.p2.area,25)
        self.assertNotEqual(self.p2.address,"128 King street")
        self.assertIsNot(self.p2.staffnum, 4)
        self.assertIsInstance(self.p2, DeliveryFnB)
        self.assertIs(self.p2.delivery_channel, "UberEat")

unittest.main(argv =[''], verbosity=2, exit= False)


# In[ ]:




