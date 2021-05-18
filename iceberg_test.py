## -*- coding: utf-8 -*-
"""
Created on Mon May 17 17:58:36 2021

@author: helena
"""

"""
Unit testing framework to ensure the model is correctly 
calculating mass of the iceberg 
"""

# Import test module and the source code that will be checked 
import unittest
import IcebergCalculations


class TestAgent(unittest.TestCase): # Identifies this class is to be tested 
        
    def test_find_mass(self):
        lidardata = ([0.0, 0.0, 0.0, 10, 100, 130, 200, 225, 178, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 10, 100, 130, 200, 225, 178, 0.0, 0.0, 0.0])
        radardata = [0.0, 0.0, 0.0, 1, 110, 133, 230, 220, 178, 0.0, 0.0, 0.0]
        seaice_m = []
        a = IcebergCalculations.IcebergCalc(lidardata, radardata, seaice_m)
        m = a.find_mass(lidardata)
        print("Check - The total mass of the iceberg is " + str(m))
        self.assertEqual(m, 1527722, "the mass of the iceberg should be 1527722")
        
        
if __name__ == '__main__': # the class runs within framework within the unittest library 
    unittest.main()