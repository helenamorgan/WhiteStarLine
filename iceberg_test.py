## -*- coding: utf-8 -*-
"""
Created on Mon May 17 17:58:36 2021

@author: helena
"""

"""
Unit testing framework to ensure the model is correctly calculating mass of the iceberg 
"""

# Import test module and the source code that will be checked 
import unittest
import IcebergCalculations


class TestAgent(unittest.TestCase): # Identifies this class is to be tested 
        
    def test_find_mass(self):
    """
    This function tests the IcebergCalculations function 'find_mass'. This function checks the mass calculations undertaken to ensure they are correct. 
    """
        lidardata = ([0.0, 0.0, 0.0, 10, 100, 130, 200, 225, 178, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 10, 100, 130, 200, 225, 178, 0.0, 0.0, 0.0]) # Lidar data list
        radardata = [0.0, 0.0, 0.0, 1, 110, 133, 230, 220, 178, 0.0, 0.0, 0.0] # Radar data list 
        seaice_m = [] # Empty list 
        a = IcebergCalculations.IcebergCalc(lidardata, radardata, seaice_m) # Defines the IcebergCalculations functions to be tested
        m = a.find_mass(lidardata) # Inputs the new lidardata list into the find_mass function
        print("Check - The total mass of the iceberg is " + str(m)) # Visually checks the correct mass is printed from the function 
        self.assertEqual(m, 1527722, "the mass of the iceberg should be 1527722") # Unit test to ensure the mass value produced is the smae 
        
        
if __name__ == '__main__': # the class runs within framework within the unittest library 
    unittest.main()