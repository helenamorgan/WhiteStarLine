# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:30:49 2021

@author: helena
"""
# Import libraries
import csv
import matplotlib.pyplot
import tkinter as tk
import IcebergCalculations2

# Pull in two data files and display them 
# Open the lidardata file and read in the data
f = open('white1.lidar.txt')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
lidardata = [] # Create an empty list to read in the data
for row in reader:
    rowlist = [] # Create an empty list for the rows of data 
    for value in row:
        rowlist.append(value) # Append the values into rows 
    lidardata.append(rowlist) # Append the rows into the list 
f.close()

# Open the radardata file and read in the data 
g = open('white1.radar.txt')
reader2 = csv.reader(g, quoting = csv.QUOTE_NONNUMERIC)
radardata = [] # Create an empty list to read in the data
for row in reader2:
    rowlist2 = [] # Create an empty list for the rows of data 
    for value in row:
        rowlist2.append(value) # Append the values into rows 
    radardata.append(rowlist2) # Append the rows into the list
f.close()

# Display the two data files 
plot1 = matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(radardata)
plot2 = matplotlib.pyplot.figure(2)
matplotlib.pyplot.imshow(lidardata)
matplotlib.pyplot.show()

# Calculate the area, volume and mass of the iceberg 
seaice_m = [] # Create an empty list for the ice values 
iceberg = IcebergCalculations2.IcebergCalc(lidardata, radardata, seaice_m) # Open the IcebergCalc class
# Assess which areas of the image are ice using the radar data 
iceberg.find_ice(radardata, seaice_m)
# Calculate the total mass of the Iceberg 
iceberg.find_mass(lidardata)
# Determine if the Iceberg can be towed
iceberg.determine_drag()

# Gather the volume, mass and whether the iceberg can be towed 
total_volume = iceberg.total_volume() # Total volume of the iceberg 
total_mass = iceberg.total_mass() # Total mass of the iceberg 
determine_drag = iceberg.determine_drag() # If the iceerg can be towed or not 

# Display the total volume, total mass and if the iceberg can towed as a GUI
window = tk.Tk()
window.wm_title("White Star Line")
title = tk.Label(window, text="White Star Line Iceberg Towing", fg='white', bg='blue')
intro = tk.Label(window, text='Calculate the mass of an iceberg and determine if it can be tugged', fg='white', bg='blue')
iceberg_volume = tk.IntVar()
iceberg_volume.set(total_volume)
iceberg_mass = tk.IntVar()
iceberg_mass.set(total_mass)
drag = tk.StringVar()
drag.set(determine_drag)
volume_text = tk.Label(window, text='The volume of the iceberg is', fg='white', bg='blue')
volume_num = tk.Label(window, text = iceberg_volume.get())
mass_text = tk.Label(window, text='The mass of the iceberg is', fg='white', bg='blue')
mass_num = tk.Label(window, text = iceberg_mass.get())
drag_text = tk.Label(window, text = drag.get())
title.pack()
intro.pack()
volume_text.pack()
volume_num.pack()
mass_text.pack()
mass_num.pack()
drag_text.pack()

#Create text file of the final iceberg data 
with open('icebergdata.txt', 'w', newline='') as tf: # tf creates a new empty text file 
    tf.write("The White Line shipping company. For this section of sea: '')
    tf.write("The total volume of the iceberg is " + str(total_volume) + '')
    tf.write("The total mass of the iceberg is " + str(total_mass) + '')
    tf.write(determine_drag)

window.mainloop()

