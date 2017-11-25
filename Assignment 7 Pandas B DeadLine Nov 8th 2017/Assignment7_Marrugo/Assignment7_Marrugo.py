#     Assigment 7 Calculation of the PXI using pandas
# import libraries
import pandas as pd
import numpy as np

# import Windows.csv file
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=0)
# import Beam irradiancie.csv file 
Beamradiance=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
# import Diffuse irradiancie.csv file 
DiffuseRadiance=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
# Set the latitude
lat=45
# selecting values from tables
ED=Beamradiance[str(lat)]["E"]
Ed=DiffuseRadiance[str(lat)]["E"]
# calculating the PXI with Fsd=0
PXIeast=1.0*(Ed+(1-0)*ED)
# salving the value of PXI in windows.csv file
windows_DF["PXI"]["east"]=PXIeast
# Creating new windows_completed_withPXI.csv file
windows_DF.to_csv("windows_completed_withPXI.csv",sep=";")