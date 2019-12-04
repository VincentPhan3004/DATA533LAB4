#!/usr/bin/env python
# coding: utf-8

# In[14]:


import unittest
from FnB.HR.StaffClass import *
from FnB.HR.HRFunction import *

class Test_HRFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Beginning Testing HRFunction Module")  
    
    @classmethod
    def tearDownClass(self):
        print("Ending Testing for HRFunction Module")
        
    def setUp(self): 
        print('Beginning a test case in HRFunction Module')
        self.p1 = Staff(12345, "Jim", "Cashier", 42345, 50000, 2017, 2017, "Tim Hortons")
        self.p2 = Manager(42345, "Tony", "Manager", 23286, 50000, 2018, 2018, "Tim Hortons",[12345,56154])
        self.p3 =Staff(32355, "Eva", "Cashier", 42345, 50000, 2015, 2016, "Tim Hortons")
       
    def tearDown(self):
        print('Finishing a test case in HRFunction Module')
                  
    def test_promoteCheck(self): # test case
        self.assertEqual(promoteCheck([self.p1,self.p2,self.p3]),[12345, 32355])
        self.assertNotEqual(promoteCheck([self.p1,self.p2]),[32355])
        self.assertIsNotNone(promoteCheck([self.p2]))
        self.assertIn(promoteCheck([self.p1,self.p2])[0],[12345, 32355,42345])
        self.assertIs(self.p2,self.p2)
        
    def test_serviceCheck(self): # test case
        self.assertEqual(serviceCheck([self.p1,self.p2,self.p3]),[32355])
        self.assertNotEqual(serviceCheck([self.p1,self.p2]),[32355])
        self.assertIsNotNone(serviceCheck([self.p2]))
        self.assertIn(serviceCheck([self.p1,self.p2])[0],[12345, 32355,42345])
        self.assertNotIn(serviceCheck([self.p3])[0],[32356,1234])
        
unittest.main(argv =[''], verbosity=2, exit= False)

