import os
import numpy as np
import pandas as pd
import scipy as sp
os.chdir("C:/Users/SilviaAnna/Desktop/scuola/building sistems/RLF Method")
windows_DF=pd.read_csv("windows.csv",sep=";",index_col=1)
def PXI_calculator(location_latitude,Direction):
    windows_BeamIrradiance=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    name_of_columnsED=windows_BeamIrradiance.columns.get_values()
    name_of_columns_as_numbersED = name_of_columnsED.astype(np.int32, copy=False)
    results_ED=sp.interp(LocationLatitude,name_of_columns_as_numbersED,windows_BeamIrradiance.loc[Direction])
    windows_DiffuseIrradiance=pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    name_of_columnsEd=windows_DiffuseIrradiance.columns.get_values()
    name_of_columns_as_numbersEd= name_of_columnsEd.astype(np.int32, copy=False)
    results_Ed=sp.interp(LocationLatitude,name_of_columns_as_numbersEd,windows_DiffuseIrradiance.loc[Direction])
    results_PXI=results_ED+ results_Ed
    return results_ED,results_Ed,results_PXI
LocationLatitude=45
ED=[]
Ed=[]
PXI=[] 
for index in windows_DF.index.tolist():    
    print index
    ED=np.append(ED,PXI_calculator(LocationLatitude,index)[0])    
    Ed=np.append(Ed,PXI_calculator(LocationLatitude,index)[1])    
    PXI=np.append(PXI,PXI_calculator(LocationLatitude,index)[2]) 
windows_DF["ED"]=ED
windows_DF["Ed"]=Ed
windows_DF["PXI"]=PXI
