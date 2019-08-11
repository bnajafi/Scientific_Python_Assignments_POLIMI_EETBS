# -*- coding: utf-8 -*-

import os
os.chdir("D:/Polimi Piacenza/Energy and Environment/notes/3 Python Files and Guidelines/assignment10_khoudari")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import psySI as SI


def weather_data_calculator(weatherDataFrame):
    deltaTheating = weatherDataFrame["Values"]["Design Heating T"]-weatherDataFrame["Values"]["Winter T"]
    deltaTcooling = weatherDataFrame["Values"]["Summer T"]-weatherDataFrame["Values"]["Design Cooling T"]
    DRcooling = weatherDataFrame["Values"]["DR"]
    latitude = weatherDataFrame["Values"]["Latitude"]
    DBT_Kelvin_outdoor = weatherDataFrame["Values"]["Summer T"]+273.15         #T in kelvin
    WBT_Kelvin_outdoor = weatherDataFrame["Values"]["Summer WBT"]+273.15
    DBT_Kelvin_indoor = weatherDataFrame["Values"]["Design Cooling T"]+273.15
    RH_indoor = weatherDataFrame["Values"]["Design Cooling RH"]
    S_outdoor = SI.state("DBT",DBT_Kelvin_outdoor,"WBT",WBT_Kelvin_outdoor,101325) # use stete func in spysi to calculate w
    W_out = S_outdoor[4]
    S_indoor = SI.state("DBT",DBT_Kelvin_indoor,"RH",RH_indoor,101325)
    W_in = S_indoor[4]
    inputsList = pd.Series([deltaTheating,deltaTcooling,DRcooling,latitude,W_out,W_in],index=["deltaTheating","deltaTcooling","DRcooling","latitude","W out","W in"])
    return inputsList
    
def U_finder(WindowsDataFrame):
    Uvalues = []
    for index in WindowsDataFrame.index.tolist():
        if WindowsDataFrame["Frame Type"][index] == "Operable":
            U_operable_DF = pd.read_csv("Ufactor_operable.csv",sep=";",index_col=0)
            U = U_operable_DF[WindowsDataFrame["Frame Material"][index]][WindowsDataFrame["Window ID"][index]]   #column, row
        elif WindowsDataFrame["Frame Type"][index] == "Fixed":
            U_fixed_DF = pd.read_csv("Ufactor_fixed.csv",sep = ";",index_col=0)
            U = U_fixed_DF[WindowsDataFrame["Frame Material"][index]][WindowsDataFrame["Window ID"][index]]
        else:
            print ('Your input for this window is not included in the library!')   
        Uvalues = np.append(Uvalues,U)
    return Uvalues    #list

def Qfen_heating_calculator(WindowsDataFrame,inputsList):
    WindowsDataFrame["U"] = U_finder(WindowsDataFrame)
    WindowsDataFrame["HF"] = WindowsDataFrame["U"]*inputsList["deltaTheating"]
    WindowsDataFrame["Qheating"] = WindowsDataFrame["Area"]*WindowsDataFrame["HF"]
    Qlist = pd.Series(WindowsDataFrame["Qheating"])
    Qtot_heating = Qlist.sum()
    return Qtot_heating

def C_value_calculator(WindowsDataFrame,inputsList):
    windowlist = pd.Series(WindowsDataFrame.index.tolist())
    numberwindow = windowlist.count()
    C_value_list = (inputsList["deltaTcooling"]-0.46*inputsList["DRcooling"])*np.ones(numberwindow)   #multiply a scalar value by a unitary vector of 4 elements
    return C_value_list

def SHGC_finder(WindowsDataFrame):
    SHGCvalues = []
    for index in WindowsDataFrame.index.tolist():
        if WindowsDataFrame["Frame Type"][index] == "Operable":
            SHGC_operable_DF = pd.read_csv("SHGC_operable.csv",sep=";",index_col=0)
            SHGC = SHGC_operable_DF[WindowsDataFrame["Frame Material"][index]][WindowsDataFrame["Window ID"][index]]
        elif WindowsDataFrame["Frame Type"][index] == "Fixed":
            SHGC_fixed_DF = pd.read_csv("SHGC_fixed.csv",sep=";",index_col=0)
            SHGC = SHGC_fixed_DF[WindowsDataFrame["Frame Material"][index]][WindowsDataFrame["Window ID"][index]]
        else:
            print ('Your input for this window is not included in the library!')   
        SHGCvalues = np.append(SHGCvalues,SHGC)
    return SHGCvalues

def Ed_finder(WindowsDataFrame,inputsList):
    Ediffuse_DF = pd.read_csv("Ediffuse.csv",sep=";",index_col=0) #import table
    latitudes = Ediffuse_DF.columns.get_values() #latitude list
    latitudes_as_numbers = latitudes.astype(np.int32, copy=False)
    Edvalues = []
    for index in WindowsDataFrame.index.tolist():
        Ed_currentvalue = sp.interp(inputsList["latitude"],latitudes_as_numbers,Ediffuse_DF.loc[WindowsDataFrame["Orientation"][index]])
        Edvalues = np.append(Edvalues,Ed_currentvalue)
    return Edvalues

def ED_finder(WindowsDataFrame,inputsList):
    Ebeam_DF = pd.read_csv("ED.csv",sep=";",index_col=0)
    latitudes = Ebeam_DF.columns.get_values()#latitude list
    latitudes_as_numbers = latitudes.astype(np.int32, copy=False)
    EDvalues = []
    for index in WindowsDataFrame.index.tolist():
        ED_currentvalue = sp.interp(inputsList["latitude"],latitudes_as_numbers,Ebeam_DF.loc[WindowsDataFrame["Orientation"][index]])
        EDvalues = np.append(EDvalues,ED_currentvalue)
    return EDvalues

def Tx_finder(WindowsDataFrame):
    for index in WindowsDataFrame.index.tolist():
        if WindowsDataFrame["Exterior Attachment"][index] == "None":
            WindowsDataFrame["Tx"][index] = 1
        elif WindowsDataFrame["Exterior Attachment"][index] == "ExteriorInsectNet":
            WindowsDataFrame["Tx"][index] = 0.64
        else:
            WindowsDataFrame["Tx"][index] = 1
            print ('Warning *  Exterior Attachment type is not known, I consider Tx to be Tx = 1.')
    return WindowsDataFrame["Tx"]

def Fshd_calculator(WindowsDataFrame,inputsList):
    SLF_DF = pd.read_csv("SLF.csv",sep=";",index_col=0)
    SLF_column = SLF_DF.columns.get_values()
    SLF_column_as_numbers = SLF_column.astype(np.int32, copy=False)     #vector (20,25,30,35...) latitude
    SLFvalues = []
    for index in WindowsDataFrame.index.tolist():
        SLF_currentvalue = sp.interp(inputsList["latitude"],SLF_column_as_numbers,SLF_DF.loc[WindowsDataFrame["Orientation"][index]])  #read table 12 for each exposure
        WindowsDataFrame["Fshd"][index] = min([1,max([0,((SLF_currentvalue*WindowsDataFrame["Doh"][index]-WindowsDataFrame["Xoh"][index])/WindowsDataFrame["Height"][index])])])
        SLFvalues = np.append(SLFvalues,SLF_currentvalue)
    WindowsDataFrame["SLF"] = SLFvalues
    return  WindowsDataFrame["Fshd"]

def PXI_calculator(WindowsDataFrame,inputsList):
    WindowsDataFrame["Tx"] = Tx_finder(WindowsDataFrame)
    WindowsDataFrame["Ed"] = Ed_finder(WindowsDataFrame,inputsList)
    WindowsDataFrame["Fshd"] = Fshd_calculator(WindowsDataFrame,inputsList)
    WindowsDataFrame["ED"] = ED_finder(WindowsDataFrame,inputsList)
    WindowsDataFrame["PXI"] = WindowsDataFrame["Tx"]*(WindowsDataFrame["Ed"]+(1-WindowsDataFrame["Fshd"])*WindowsDataFrame["ED"])
    return WindowsDataFrame["PXI"] 

def FFs_finder(WindowsDataFrame):
    FFs_DF = pd.read_csv("FFs.csv",sep=";",index_col=0)
    FFsvalues =[]
    for index in WindowsDataFrame.index.tolist():
        TypeBuilding = WindowsDataFrame["Type Building"][index]
        if TypeBuilding == "Single Family Detached":
            FFs_currentvalue =  FFs_DF["Single Family Detached"][WindowsDataFrame["Orientation"][index]]
        elif TypeBuilding == "Multifamily":
            FFs_currentvalue =  FFs_DF["Multifamily"][WindowsDataFrame["Orientation"][index]]
        else:
            print ('Warning *  Building type is not known')
        FFsvalues = np.append(FFsvalues,FFs_currentvalue)
    return FFsvalues

def IAC_calculator(WindowsDataFrame):
    IACcl_DF = pd.read_csv("IACcl.csv",sep=";",index_col=0)
    IACclvalues = []
    for index in WindowsDataFrame.index.tolist():
        if (WindowsDataFrame["IntShading ID"][index] in IACcl_DF.columns.tolist()):
            IACcl = IACcl_DF[WindowsDataFrame["IntShading ID"][index]][WindowsDataFrame["Window ID"][index]]
        else:9
        print ('The interior shading for this window is not included in the library')
        WindowsDataFrame["IAC"][index] = 1.0+WindowsDataFrame["Fcl"][index]*(IACcl-1.0)
        IACclvalues = np.append(IACclvalues,IACcl)
    WindowsDataFrame["IACcl"] = IACclvalues
    return WindowsDataFrame["IAC"]

def Qfen_cooling_calculator(WindowsDataFrame,inputsList):
    WindowsDataFrame["U"] = U_finder(WindowsDataFrame)
    WindowsDataFrame["C_value"] = C_value_calculator(WindowsDataFrame,inputsList)
    WindowsDataFrame["PXI"] = PXI_calculator(WindowsDataFrame,inputsList)
    WindowsDataFrame["SHGC"] = SHGC_finder(WindowsDataFrame)    
    WindowsDataFrame["IAC"] = IAC_calculator(WindowsDataFrame)
    WindowsDataFrame["FFs"] = FFs_finder(WindowsDataFrame)
    WindowsDataFrame["CF"] = WindowsDataFrame["U"]*WindowsDataFrame["C_value"]+WindowsDataFrame["PXI"]*WindowsDataFrame["SHGC"]*WindowsDataFrame["IAC"]*WindowsDataFrame["FFs"]
    WindowsDataFrame["Qcooling"] = WindowsDataFrame["Area"]*WindowsDataFrame["CF"]
    Qlist = pd.Series(WindowsDataFrame["Qcooling"])
    Qtot_cooling = Qlist.sum()
    return Qtot_cooling