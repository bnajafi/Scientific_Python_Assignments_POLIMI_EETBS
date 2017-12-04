# Guidelines for Assignment 8
import os
import numpy as np
import pandas as pd

import scipy as sp # You need to import Scipy in order to interpolate
os.chdir ("C:\Users\Marica\Desktop\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")


#  the procedure to find the IAC_cl of all windows:
windows_DataFrame = pd.read_csv("windows.csv",sep=";",index_col= 0)


DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)

# Defining a function that read IAC_cl from the Table
def IAC_CL_finder(windowID,IntShadingID):
    DF_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col=1)
    IAC_cl_value= DF_IAC_cl[IntShadingID][windowID]
    return IAC_cl_value
    
    

# writing a for loop to do the look up of IAC_cl for all windows using the developed function
IAC_values=[]
for index in windows_DataFrame.index.tolist():
    print index
    IAC_values = np.append(IAC_values,IAC_CL_finder(windows_DataFrame["Window_ID"][index],windows_DataFrame["IntShading_ID"][index]))
        
        
# You should use the demosntrated prcedure to find and update the PXI of all windows!



# How to interpolate !

# if df_BeamIrradiance is your DataFrame:
#pay attention that you should add a code to create df_BeamIrradiance using read_csv

Latitude=42
name_of_columns=df_BeamIrradiance.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

# for thedirection of South
ED=sp.interp(Latitude,name_of_columns_as_numbers,df_BeamIrradiance.loc["S"]) # pay attention that you should have scipy imported as sp in the beggining 

# you use the same procedure for the diffuse one 






    