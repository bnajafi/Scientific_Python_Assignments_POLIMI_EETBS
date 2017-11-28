import os
import pandas as pd
import numpy as np

os.chdir ("C:\Users\TOSHIBA\Documents\Italia\Building\Git\git_fork\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\Assignment7_Wong")

latitude_location="45"
beam_irra = pd.read_csv("beamIrradiance.csv",sep=";",index_col=0)
diffuse = pd.read_csv("diffuseIrradiance.csv",sep = ";",index_col=0)
windows = pd.read_csv("windows.csv",sep=";",index_col=0)

print beam_irra.columns
print beam_irra.index
print diffuse.columns
print diffuse.index
print windows.columns
print windows.index

windows.loc["east","PXI"]=beam_irra.loc["E",latitude_location]+diffuse.loc["E",latitude_location]
print windows.loc["east","PXI"]

# How to write the modified Table to a new file.
windows.to_csv("windows_completed_withPXI.csv",sep=";")
