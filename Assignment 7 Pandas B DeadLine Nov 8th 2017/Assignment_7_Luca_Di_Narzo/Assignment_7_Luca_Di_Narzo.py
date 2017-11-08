import os
import pandas as pd
import numpy as np
os.chdir('C:\Users\Utente\Desktop\Building\RLF Method')

latitude_location=45

Tx=1

Beam_irr=pd.read_csv('BeamIrradiance.csv',sep=';',index_col=0)
Diffuse_irr=pd.read_csv('DiffuseIrradiance.csv',sep=';',index_col=0)
windows_DF = pd.read_csv("windows_completed1.csv",sep=";",index_col=0)

#I'm going to resolve this assignment in 2 ways

#1st way: Defining all the variables for west and south
ED_south=Beam_irr['45']['S']
ED_west=Beam_irr['45']['W']
Ed_south=Diffuse_irr['45']['S']
Ed_west=Diffuse_irr['45']['W']

Et_south=ED_south+Ed_south
Et_west=ED_west+Ed_west

PXI_south=Tx*Et_south
PXI_west=Tx*Et_west

#2nd way: For east i will resolve everithing in one stream
PXI_east=Tx*(Beam_irr['45']['E']+Diffuse_irr['45']['E'])

windows_DF['PXI']['east']=PXI_east
windows_DF['PXI']['west']=PXI_west
windows_DF['PXI']['south-Fixed']=PXI_south
windows_DF['PXI']['south-Operable']=PXI_south

windows_DF.to_csv("windows_completed1_withPXI.csv",sep=";")