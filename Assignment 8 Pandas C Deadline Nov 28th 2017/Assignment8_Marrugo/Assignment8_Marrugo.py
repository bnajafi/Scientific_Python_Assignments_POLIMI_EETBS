#     Assigment 8 Calculation of the PXI using pandas and functions
# import libraries
import pandas as pd
import numpy as np
import scipy as sp

def PXIcalculator(Lat,SunDirection,Tx):
    # import Beam irradiancie.csv file 
    Beamradiance=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    # import Diffuse irradiancie.csv file 
    DiffuseRadiance=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    # Interpolation of the latitude Beam Irradiance
    NameColumBI=Beamradiance.columns.get_values()
    NumberColumns = NameColumBI.astype(np.int32, copy=False)
    # Interpolation of the latitude Diffuse Irradiance
    NameColumDI=DiffuseRadiance.columns.get_values()
    NumberColumns2 = NameColumDI.astype(np.int32, copy=False)
    # selecting values from tables
    ED=sp.interp(int(Lat),NumberColumns,Beamradiance.loc[SunDirection]) 
    Ed=sp.interp(int(Lat),NumberColumns2,DiffuseRadiance.loc[SunDirection])
    # calculating the PXI with Fsd=0 
    PXI=Tx*(Ed+(1-0)*ED)
    return PXI

# import Windows.csv file
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
PXIs=[]
for index in windows_DF.index:
    latitude=45
    PXI=PXIcalculator(latitude,windows_DF["Direction"][index],windows_DF["Tx"][index])
    PXIs=np.append(PXIs,PXIcalculator(latitude,windows_DF["Direction"][index],windows_DF["Tx"][index]))
    print index,PXI
#save PXI values in windows    
windows_DF["PXI"]=PXIs  
#export the values of windows to csv  
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")
