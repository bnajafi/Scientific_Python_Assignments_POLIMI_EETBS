#Assignment 7

import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\MonicaDepp\Dropbox\GitBash\gitForkClone\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 7 Pandas B DeadLine Nov 8th 2017\__Guidelines__")


latitude_location=45    #setting the latitude at 45 degrees

#reading the .csv files:
windows_DF=pd.read_csv("windows.csv",sep=';',index_col=0)
beamIrradiance_DF=pd.read_csv("beamIrradiance.csv",sep=';',index_col=0)
diffuseIrradiance_DF=pd.read_csv("diffuseIrradiance.csv",sep=';',index_col=0)

print windows_DF.columns
print windows_DF.index
print beamIrradiance_DF.columns
print beamIrradiance_DF.index
print diffuseIrradiance_DF.columns
print diffuseIrradiance_DF.index

#extracting the values for the eastern side:
beam_irr_value= beamIrradiance_DF.loc["E",str(latitude_location)]
diff_irr_value= diffuseIrradiance_DF.loc["E",str(latitude_location)]

#I know these calculations are useless and not necessary when we have no external shading, I just wanted to try making them.
SLF=windows_DF.loc['east','SLF']
Xoh=windows_DF.loc['east','Xoh']
Doh=windows_DF.loc['east','Doh']
h=windows_DF.loc['east','Height']
Fshd=min(1,max(0,(SLF*Doh-Xoh)/h))
Tx=windows_DF.loc['east','Tx']

#PXI:
PXI=Tx*(diff_irr_value+(1-Fshd)*beam_irr_value)
print PXI

#updating the PXI column in windows dataframe:
windows_DF["PXI"] = np.array([PXI,0,0,0])

#writing the modified table to a new file:
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")