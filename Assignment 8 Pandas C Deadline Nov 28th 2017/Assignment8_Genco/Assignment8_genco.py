import os
import numpy as np
import pandas as pd
import scipy as sp

os.chdir ("/Users/FedericoGenco/Desktop/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 7 Pandas B DeadLine Nov 8th 2017/__Guidelines__")

def Irradiance (latitude,direction): 
    Idirect_dataFrame=pd.read_csv ("BeamIrradiance.csv", sep=";",  index_col=0)
    Idiffuse_dataFrame=pd.read_csv ("DiffuseIrradiance.csv", sep=";",  index_col=0)
    name_of_columns=Idirect_dataFrame.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Idirect=sp.interp(latitude,name_of_columns_as_numbers,Idirect_dataFrame.loc[direction])
    name_of_columns1=Idiffuse_dataFrame.columns.get_values()
    name_of_columns_as_numbers1 = name_of_columns.astype(np.int32, copy=False)
    Idiffuse=sp.interp(latitude,name_of_columns_as_numbers1,Idiffuse_dataFrame.loc[direction])
    PXI=Idirect+Idiffuse
    return Idiffuse, Idirect, PXI
    
windows_ID=pd.read_csv ("windows.csv", sep=";" , index_col=1)
PXI_values=[]
for i in windows_ID.index.tolist():
    print i
    values=Irradiance ("45",i)
    PXI_values.append(values[2])
    print "Ed,ED, PXI: " +str(values)
    
print PXI_values

windows_ID["PXI"]=PXI_values
windows_ID.to_csv("windows_Ass8_withPXI.csv",sep=";")





   

    

