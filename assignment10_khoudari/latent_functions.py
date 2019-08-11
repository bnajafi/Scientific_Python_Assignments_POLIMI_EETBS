# -*- coding: utf-8 -*-

import os
os.chdir("D:/Polimi Piacenza/Energy and Environment/notes/3 Python Files and Guidelines/assignment10_khoudari")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import psySI as SI



#Internal Gains, Latent Load

def Qig_l_Calculation(Acf,Nbr):
    A = Acf
    No = Nbr + 1
    Qig_l = 20 + 0.22 * A + 12 * No
    return  Qig_l


#Infiltration, Latent Load

def Leakage_Area_calc(Exposed_surf_Area, type_of_construction):
    unit_leakage_Area = pd.read_csv("Leakage_Area.csv", sep = ";", index_col=0)
    As = Exposed_surf_Area
    Al = unit_leakage_Area["Aul "][type_of_construction]
    LeaK_Area = Al*As
    return LeaK_Area
       
def Idf_Cooling_calc(h_house, T_outdoor_cooling):
    idf_table_cooling=pd.read_csv("IDF_cooling.csv",sep = ";",index_col=0)
    name_of_columns=idf_table_cooling.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    name_of_index=idf_table_cooling.index.get_values()
    name_of_index_as_numbers = name_of_index.astype(float)
    t_outdoor=T_outdoor_cooling
    height=h_house
    if height<=2.4:
        h=2.4
    elif 3>=height>2.4:
        h=3
    elif 4>=height>3:
        h=4
    elif 5>=height>4:
        h=5
    elif 6>=height>5:
        h=6      
    elif 7>=height>6:
        h=7
    elif 8>=height>7:
        h=8        
    s=[40]   
    m=10
    for value in name_of_columns_as_numbers:
        if t_outdoor<=value:
            s.append(value)
    IDF1=min(s)
    for value in name_of_columns_as_numbers:
        if value<=t_outdoor<=IDF1:
            m=value
    IDF2=m
    t1=str(IDF2)
    t2=str(IDF1)
    IDF1=idf_table_cooling[t1][h]
    IDF2=idf_table_cooling[t2][h]
    IDF_final=(IDF1+IDF2)/2
    return IDF_final
    
def inf_flowrate(Exposed_surf_Area, type_const, h_house, T_outdoor):
    Al_cooling = Leakage_Area_calc(Exposed_surf_Area,type_const)
    IDF_cooling = Idf_Cooling_calc(h_house,T_outdoor)
    inf_flowrate = Al_cooling * IDF_cooling
    return  inf_flowrate 

#Ventilation, Latent Load

def vent_flowrate(A_conditioned_floor, n_br):
    A = A_conditioned_floor
    Nbr = n_br
    ven_flowrate = 0.05 * A + 3.5 * (Nbr+1)
    return ven_flowrate
    

#Combined Infiltration and  Ventilation, Latent Load

def qlat_infvent_calc(input_data_inf_vent, weatherResults):
     #read values from tables
     vol = float(input_data_inf_vent.iloc[0][0])
     Aes = float(input_data_inf_vent.iloc[1][0])
     Type_cons = input_data_inf_vent.iloc[2][0]
     Design_cond = input_data_inf_vent.iloc[3][0]
     H_house = float(input_data_inf_vent.iloc[4][0])
     Dt_heating = float(input_data_inf_vent.iloc[5][0])
     Dt_cooling = float(input_data_inf_vent.iloc[6][0])
     Al = float(input_data_inf_vent.iloc[7][0])
     A_cond_floor = float(input_data_inf_vent.iloc[8][0])
     Nbr = float(input_data_inf_vent.iloc[9][0])
     Vent_supp_air_fr = input_data_inf_vent.iloc[10][0]
     Vent_ex_air_fr = input_data_inf_vent.iloc[11][0]
     Cs = float(input_data_inf_vent.iloc[12][0])
     Eps = float(input_data_inf_vent.iloc[13][0])
     Q_bal_fr = float(input_data_inf_vent.iloc[14][0])
     Q_bal_ot_fr = float(input_data_inf_vent.iloc[15][0])
     Hrv_Erv = input_data_inf_vent.iloc[16][0]
     Cl = float(input_data_inf_vent.iloc[17][0])
     Humidity_difference = input_data_inf_vent.iloc[18][0]
     Ct = float(input_data_inf_vent.iloc[19][0])
     Eps_tot = input_data_inf_vent.iloc[20][0]
     H_difference = input_data_inf_vent.iloc[21][0]
     #calculations
     deltaW = weatherResults.iloc[4] - weatherResults.iloc[5]
     inf_cooling = inf_flowrate(Aes, Type_cons, H_house, Dt_cooling)
     vent_cooling = vent_flowrate(A_cond_floor, Nbr)
     infvent_cooling = inf_cooling + vent_cooling
     qlat_infvent_cool = Cl * (infvent_cooling + Q_bal_ot_fr) * deltaW
     return qlat_infvent_cool
     

#Total Latent Load

def Qtot_latent (input_data_inf_vent, weatherResults):
    A_cond_floor = float(input_data_inf_vent.iloc[8][0])
    Nbr = float(input_data_inf_vent.iloc[9][0])
    intgain_lat = Qig_l_Calculation(A_cond_floor,Nbr)
    infvent_lat = qlat_infvent_calc(input_data_inf_vent, weatherResults)
    qlat = intgain_lat + infvent_lat
    return qlat
 
 