#!/usr/bin/env python
# coding: utf-8

# In[39]:


import unittest
from FnB.HR.StaffClass import *

class Test_StaffClass(unittest.TestCase): # test class
    @classmethod
    def setUpClass(cls):
        print("Beginning StaffClass Testing")  
    
    @classmethod
    def tearDownClass(self):
        print("Ending StaffClass Testing")
        
    def setUp(self): 
        print('Begin a test case in Test_StaffClass')
        self.p1 = Staff(12345, "Jim", "Cashier", 42345, 50000, 2017, 2017, "Tim Hortons")
        self.p2 = Manager(42345, "Tony", "Manager", 23286, 50000, 2016, 2018, "Tim Hortons",[12345,56154])
        
    def tearDown(self):
        print('Finish a test case in Test_StaffClass')
                
    def test_Staff(self): # test case
        self.assertEqual(self.p1.ID,12345)
        self.assertNotEqual(self.p1.name,"Tony")
        self.assertIsNot(self.p1.title,"Waitress")
        self.assertIsNotNone(self.p1.entry_year)
        self.assertIsInstance(self.p1,Staff)
    
    def test_Manager(self): # test case
        self.assertEqual(self.p2.ID,42345)
        self.assertNotEqual(self.p2.name,"Tommy")
        self.assertIsNot(self.p2.title,"Casher")
        self.assertIn(self.p1.ID,self.p2.stafflist)
        self.assertIsInstance(self.p2,Manager)
        
unittest.main(argv =[''], verbosity=2, exit= False)

