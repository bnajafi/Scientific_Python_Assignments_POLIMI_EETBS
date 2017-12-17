
import os
os.chdir("D:/Polimi Piacenza/Energy and Environment/notes/3 Python Files and Guidelines/assignment10_khoudari")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp


def R_input_calculator(inputWalls,materials): 
    for index in inputWalls.index.tolist():
        currentMterialID = inputWalls["material ID"][index]
        if inputWalls["Type"][index] == "conv":
            inputWalls["Rvalue"][index] = materials["R"][currentMterialID]            
        elif inputWalls["Type"][index] == "cond":
            inputWalls["Rvalue"][index] = materials["R"][currentMterialID] * inputWalls["lenght"][index] / materials["Thickness"][currentMterialID]            
        else:
            print  "I can't calculate this resistance value"        
    return inputWalls
     
     
def U_wall_calculator(inputWalls) :               
    list_series = []    
    for res in inputWalls.index.tolist():
        if inputWalls["Area Percentage"][res] == 1:
            list_series = np.append(list_series,inputWalls["Rvalue"][res])            
        else:
            pass            
    list_parallel = []       
    for res in inputWalls.index.tolist():
        if inputWalls["Area Percentage"][res]!=1:
            list_series1=np.append(list_series,inputWalls["Rvalue"][res])
            R=list_series1.sum()
            U=inputWalls["Area Percentage"][res]/R
            list_parallel=np.append(list_parallel, U)           
        else:
            pass   
    List_parallel_pandas=pd.Series(list_parallel)
    U_value=List_parallel_pandas.sum()  
    return U_value
    
    
def Utot_wall_Calculator(inputDF,materials):
    inputDF=R_input_calculator(inputDF,materials)
    Utot=U_wall_calculator(inputDF)
    return Utot
    

def U_door_calculator(inputWalls) :               
    list_series=[]    
    for res in inputWalls.index.tolist():
        if inputWalls["Area Percentage"][res]==1:
            list_series=np.append(list_series,inputWalls["Rvalue"][res])            
        else:
            pass   
    R_value=list_series.sum()
    Uvalue=1.0/R_value
    return Uvalue
    
    
def Utot_door_Calculator(inputDF,materials):
    inputDF=R_input_calculator(inputDF,materials)
    Utot=U_door_calculator(inputDF)
    return Utot    

    
def QtotOpaque_summer_calculator(h_windows,w_windowsS,w_windowsE,w_windowsW,UWallSummer,UCeiling,UDoorSummer,colourRoof,materialRoof,deltaTCooling,DRcooling,wallsSurfaceType,ceilingSurfaceType,doorsSurfaceType):
    opaque_DataFrame = pd.read_csv("input_opaque.csv",sep=";",index_col= 0)
    Areas = Area_calculator(h_windows,w_windowsS,w_windowsE,w_windowsW)
    opaque_DataFrame["Area"]=Areas    
    opaque_DataFrame["Usummer"]=[UWallSummer,UCeiling,UDoorSummer]
    alfa_DataFrame = pd.read_csv("alfa_value.csv",sep=";",index_col= 0)
    alfa_roof=alfa_DataFrame[colourRoof][materialRoof]
    OF_DataFrame = pd.read_csv("OF_values.csv",sep=";",index_col= 0)
    OFb_1=14.3*alfa_roof-4.5
    OFb_2=38.3*alfa_roof-7
    OF_DataFrame["OFb"]=[OFb_1,OFb_2,8.2,0,0,0]
    OF_DataFrame["CF/U"]=OF_DataFrame["OFt"]*deltaTCooling+OF_DataFrame["OFb"]+OF_DataFrame["OFr"]*DRcooling
    CF_walls=OF_DataFrame["CF/U"][wallsSurfaceType]*opaque_DataFrame["Usummer"]["Walls"]
    CF_ceiling=OF_DataFrame["CF/U"][ceilingSurfaceType]*opaque_DataFrame["Usummer"]["Ceiling"]
    CF_doors=OF_DataFrame["CF/U"][doorsSurfaceType]*opaque_DataFrame["Usummer"]["Doors"]
    opaque_DataFrame["CF"]=[CF_walls,CF_ceiling,CF_doors]
    opaque_DataFrame["Q_summer"]=opaque_DataFrame["CF"]*opaque_DataFrame["Area"]
    Qtot_Opaque_summer=opaque_DataFrame["Q_summer"].sum()
    return Qtot_Opaque_summer
    

def Area_calculator(h_windows,w_windowsS,w_windowsE,w_windowsW):
    opaque_DataFrame = pd.read_csv("input_opaque.csv",sep=";",index_col= 0)
    AtotWindows=h_windows*(w_windowsS+w_windowsE+w_windowsW)
    opaque_DataFrame.iloc[1:,2]= opaque_DataFrame["width"] *opaque_DataFrame["h"] 
    opaque_DataFrame["Area"]["Walls"]= opaque_DataFrame["width"]["Walls"] *opaque_DataFrame["h"]["Walls"] - AtotWindows - opaque_DataFrame["Area"]["Doors"]
    areas=opaque_DataFrame["Area"]
    return areas


def QtotOpaque_winter_calculator(h_windows,w_windowsS,w_windowsE,w_windowsW,UWallWinter,UCeiling,UDoorWinter,deltaTHeating):
    opaque_DataFrame = pd.read_csv("input_opaque.csv",sep=";",index_col= 0)
    Areas= Area_calculator(h_windows,w_windowsS,w_windowsE,w_windowsW)
    opaque_DataFrame["Area"]=Areas
    opaque_DataFrame["Uwinter"]=[UWallWinter,UCeiling,UDoorWinter]
    opaque_DataFrame["HF"]=opaque_DataFrame["Uwinter"]*deltaTHeating
    opaque_DataFrame["Q_winter"]=opaque_DataFrame["HF"]*opaque_DataFrame["Area"]
    opaque_DataFrame.to_csv("opaque_DataFrame_modified.csv")
    Qtot_Opaque_winter=opaque_DataFrame["Q_winter"].sum()
    return Qtot_Opaque_winter

