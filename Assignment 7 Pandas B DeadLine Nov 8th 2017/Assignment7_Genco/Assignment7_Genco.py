import os
import pandas as pd
import numpy as np

os. chdir ("/Users/FedericoGenco/Desktop/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 7 Pandas B DeadLine Nov 8th 2017/__Guidelines__")   #import the file

BeamIrradiance=pd.read_csv ("BeamIrradiance.csv", sep=";", index_col=0)                    #assign to the matrix BeamIradiance the values of the file
DiffusiveIrradiance=pd.read_csv ("DiffuseIrradiance.csv", sep=";" , index_col=0)

Ed=DiffusiveIrradiance["45"]["E"]
ED=BeamIrradiance ["45"]["E"]
Tx=1

PXI=Tx*(ED+Ed)

windows=pd.read_csv ("windows.csv", sep=";", index_col=0)
 
windows["PXI"]=np.array([PXI,0,0,0])

windows.to_csv("windows_completed_withPXI.csv",sep=";")