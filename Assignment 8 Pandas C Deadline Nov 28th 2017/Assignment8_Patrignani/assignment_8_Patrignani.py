import os
import numpy as np
import pandas as pd
import scipy as sp

os.chdir("C:/Users/stefy/Desktop/POLIMI/I ANNO/1 Semestre/Buildings/Lectures/LESSON 7 RLF Method")

windows_DataFrame = pd.read_csv("windows.csv", sep=";", index_col = 0)              #reading windows data from tables
df_BeamIrradiance = pd.read_csv("BeamIrradiance.csv", sep=";", index_col = 0)       #reading irradiance data from table
diff_irr = pd.read_csv("DiffuseIrradiance.csv", sep=";", index_col = 0)             #reading irradiance data from table

name_of_columns_B=df_BeamIrradiance.columns.get_values()                            #defining names of columns for interpolation (for beam irradiance)
name_of_columns_as_numbers_B = name_of_columns_B.astype(np.int32, copy=False)

name_of_columns_D=diff_irr.columns.get_values()                                     #defining names of columns for interpolation (for diffuse irradiance)
name_of_columns_as_numbers_D = name_of_columns_D.astype(np.int32, copy=False)


def Et_calculator (latitude,orientation):                                          #defining a function that gives me the PXI value given the latitude & the orientation of the wall
    beam_irr = sp.interp(latitude, name_of_columns_as_numbers_B, df_BeamIrradiance.loc[orientation])        #interpolation function for beam irradiance
    
    diff_ir = sp.interp(latitude, name_of_columns_as_numbers_D, diff_irr.loc[orientation])                  #interpolation function for diffuse irradiance

    Et = beam_irr + diff_ir
    return Et
    
# writing a 'for' loop to calculate the PXI for all windows using the developed function
latitude = 45   #Piacenza
Et = []
for index in windows_DataFrame.index.tolist():
    
    Et = np.append(Et, Et_calculator([latitude],windows_DataFrame["Direction"][index]))                     #calculate the PXI value of each windows running the previuos function changing the index: directon for each iteration (latitude is constant) 

PXI = Et * windows_DataFrame["Tx"]          #real PXI value is Et * Tx (neglecting external shading)
print PXI

#modifing the table windows with the new vector containing the new value of PXI 
windows_DataFrame["PXI"] = PXI

#writing new modified table
windows_DataFrame.to_csv("windows_completedWithPXI_final.csv",sep=";")