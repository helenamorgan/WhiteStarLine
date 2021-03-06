# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:32:58 2021

@author: helena
"""

class IcebergCalc():
    """
    Class declaration for the IcebergCalc class.
    Provides methods for calculating an iceberg's area, volume and mass.
    """
    
    
    def __init__(self, lidardata, radardata, seaice_m):
        """
        Constructor function initialises the attributes of the IcebergCalc class.

        Parameters
        ----------
        lidardata : list of intergers
            List of the lidar data
        radardata : list of integers
            List of the radar data 
        seaice_m : list 
            Empty list for the ice variables to be appended

        Returns
        -------
        None.

        """
        self.lidardata = lidardata
        self.radardata = radardata
        self.seaice_m = []
    
    def find_ice(self, radardata, seaice_m):
        """
        This function finds if there is ice within this section of the sea. 
        Ice has radar data values of over 100, so this function finds those values over 100 and prints these values. 

        Parameters
        ----------
        radardata : list of integers
            List of the radar data 
        seaice_m : list
            Empty list for the ice variables to be appended. The default is None.

        Returns
        -------
        None.

        """
        for i in range(len(radardata)):
            if i >= 100.0:
                seaice_m.append(i)
        print("Areas of ice are " + str(seaice_m))
        
        #print(seaice_m)
    
    def find_mass(self, lidardata):
        """
        This function calculates the area, volume and mass of the ice. 
        The lidar data is in cm. 
        The area of the icberg is calculated then multiplied by the by the height to calculate the volume. 
        The volume is multiplied by the density of ice to calculate the mass of the iceberg. 
        The density of ice is a set value. 
        The total volume of the mass of the iceberg is calculated by multiplying by 10 (as only 10% of the iceberg is currently above the water line) to calculate 100% of the iceberg mass. 
        These variables are printed. 
        

        Parameters
        ----------
        lidardata : list of integers
            List of the lidar data 

        Returns
        -------
        Integer.
            The total mass of the iceberg. 
        """
        global total_volume
        global total_mass
        total_pixels = 0
        total_volume = 0
        for row in lidardata:
            for i in row:
                if i >= 100.0:
                    total_pixels += 1 # Area of the iceberg
                    total_volume += i*0.1 # Convert cm to m as 0.1 = 10cm 
        # Density of ice = 917km/m^3
        iceberg_mass = total_volume * 917
        total_mass = iceberg_mass * 10
        print("The area of iceberg is" + " " + str(total_pixels) + " m^2")
        print("The volume of iceberg is" + " " + str(total_volume) + " m^3")
        print("The mass of the iceberg is" + " " + str(iceberg_mass) + " kg/m^3")
        print("The total mass of the iceberg is" + " " + str(total_mass) + " kg/m^3")
        return(total_mass)
    
    def total_volume(self):
        """
        This function defines the variable total volume of the iceberg. 

        Returns
        -------
        Integer
            The total volume of the iceberg.

        """
        return int(total_volume)
    
    def total_mass(self):
        """
        This function defines the variable total mass of the iceberg.

        Returns
        -------
        Integer
            The total mass of the iceberg.

        """
        return int(total_mass)
        
    def determine_drag(self):
        """
        This function determines whether the iceberg is within size range to be towed by the company tug boat. 
        If the iceberg is larger than 36 million kg in mass, it cannot be towed by the tug boat. 

        Returns
        -------
        String .
            If the iceberg is within size range to be towed by the company. 
        """
        global within_range
        global outside_range
        within_range = "Can tow iceberg"
        outside_range = "Cannot tow iceberg" 
        if total_mass > 36000000:
            return(outside_range)
        return(within_range)
            
    