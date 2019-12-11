#!/usr/bin/env python
# coding: utf-8

# In[20]:


import unittest
from FnB.OP.FnBClass import *
from FnB.OP.FnBFunction import *

class Test_FnBFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Beginning Testing FnBFunction Module")  
        
    @classmethod
    def tearDownClass(self):
        print("Ending Testing for FnBFunction Module")
        
    def setUp(self): 
        print('Beginning a test case in FnBFunction Module')
        self.p1 = FnB("145 Ponto road", 145, 135000, 10)
        self.p2 = DeliveryFnB("129 King street", 25, 85000, 3,"UberEat")
        self.p3 = FnB("138 North Street", 126, 140000, 12)
    
    def tearDown(self):
        print('Finishing a test case in FnBFunction Module')
    
    def test_compare(self): # test case
        self.assertEqual(compare(self.p1,self.p2),self.p2)
        self.assertNotEqual(compare(self.p1, self.p3),self.p1)
        self.assertIsNotNone(compare(self.p2, self.p3))
        self.assertIs(self.p2,self.p2)
        self.assertIsNot(self.p3, self.p1)
    
    def test_serviceCheck(self): # test case
        self.assertEqual(staffTransfer(self.p1, self.p2, 2), True)
        self.assertNotEqual(staffTransfer(self.p3, self.p2, 20), True)
        self.assertTrue(staffTransfer(self.p2, self.p1, 1))
        self.assertFalse(staffTransfer(self.p2, self.p1, 20))
        self.assertIs(staffTransfer(self.p3, self.p2, 2), True)
        
unittest.main(argv =[''], verbosity=2, exit= False)
        
                


# In[ ]:




