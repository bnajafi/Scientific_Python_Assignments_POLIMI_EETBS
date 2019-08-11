import os
os.chdir("D:/Polimi Piacenza/Energy and Environment/notes/3 Python Files and Guidelines/assignment10_khoudari")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import psySI as SI


#Internal Gain, Sensible Load

def Qig_s_Calculation(Acf,Nbr):
    A = Acf
    No = Nbr+1
    Qig_s = 136 + 2.2*A + 22*No
    return  Qig_s


#Infiltration, Sensible Load

def Leakage_Area_calc(Exposed_surf_Area,type_of_construction):
    unit_leakage_Area = pd.read_csv("Leakage_Area.csv",sep = ";",index_col=0)
    As = Exposed_surf_Area
    Al = unit_leakage_Area["Aul "][type_of_construction]
    LeaK_Area = Al*As
    return LeaK_Area

def Idf_Heating_calc(h_house,T_outdoor_heating):
    idf_table_heating = pd.read_csv("IDF_heating.csv",sep = ";",index_col=0)
    name_of_columns = idf_table_heating.columns.get_values()#(-40,-30...)
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    name_of_index = idf_table_heating.index.get_values()
    name_of_index_as_numbers = name_of_index.astype(float)
    height = h_house
    if height <= 2.5:    #excess approximation
        h = 2.5
    elif 3 >= height > 2.5:
        h = 3
    elif 4 >= height > 3:
        h = 4
    elif 5 >= height > 4:
        h = 5
    elif 6 >= height > 5:
        h = 6      
    elif 7 >= height > 6:
        h = 7
    elif 8 >= height > 7:
        h = 8        
    t_heat = T_outdoor_heating    #-4,8
    s = [0]
    for value in name_of_columns_as_numbers:
      if value >= t_heat:
         s.append(value)    #value can be -40,-30,-20
    IDF1 = min(s)  #value at the right side of my Temperature, for us is 0 
    m = 0
    for value in name_of_columns_as_numbers:
       if value<=t_heat<=IDF1 :
          m = value
    IDF2 = m     #out from the for cycle, so only with the last one, so only with the value at the left side of my Temperature, for us -10
    t1 = str(IDF2)
    t2 = str(IDF1)
    IDF1_f = float(idf_table_heating[t1][h])
    IDF2_f = float(idf_table_heating[t2][h])   #take the 2 value in the table, but inputs are string
    IDF_final = (IDF1_f+IDF2_f)/2        #average value is final value  
    return IDF_final   

def inf_air_flo_rate_heat_calc(Exposed_surf_Area,type_const,h_house,T_outdoor): 
    Al_heating = Leakage_Area_calc(Exposed_surf_Area,type_const)
    IDF_heating = Idf_Heating_calc(h_house,T_outdoor)
    inf_air_flo_rate_heat = Al_heating * IDF_heating
    return inf_air_flo_rate_heat

def Idf_Cooling_calc(h_house,T_outdoor_cooling):
    idf_table_cooling = pd.read_csv("IDF_cooling.csv",sep = ";",index_col=0)   
    name_of_columns = idf_table_cooling.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    name_of_index = idf_table_cooling.index.get_values()
    name_of_index_as_numbers = name_of_index.astype(float)
    t_outdoor = T_outdoor_cooling
    height = h_house
    if height <= 2.5:     #excess approximation
        h = 2.5
    elif 3 >= height > 2.5:
        h = 3
    elif 4 >= height > 3:
        h = 4
    elif 5 >= height > 4:
        h = 5
    elif 6 >= height > 5:
        h = 6      
    elif 7 >= height > 6:
        h = 7
    elif 8 >= height > 7:
        h = 8      
    s = [40]
    m = 10
    for value in name_of_columns_as_numbers: 
      if t_outdoor <= value:
         s.append(value)
    IDF1 = min(s)  #value on the right respect to ours
    for value in name_of_columns_as_numbers:
        if value <= t_outdoor <= IDF1:
           m = value
    IDF2 = m     #value on left side
    t1 = str(IDF2)
    t2 = str(IDF1)
    IDF1 = idf_table_cooling[t1][h]
    IDF2 = idf_table_cooling[t2][h]
    IDF_final = (IDF1+IDF2)/2
    return IDF_final

def inf_air_flo_rate_cool_calc(Exposed_surf_Area,type_const,h_house,T_outdoor):
    Al_cooling = Leakage_Area_calc(Exposed_surf_Area,type_const)
    IDF_cooling = Idf_Cooling_calc(h_house,T_outdoor)
    inf_air_flo_rate_cool = Al_cooling * IDF_cooling
    return inf_air_flo_rate_cool 
    

#Ventilation, Sensible Load

def vent_flow_rate(A_conditioned_floor,n_br):
    A = A_conditioned_floor
    Nbr = n_br
    V_flow_rate = 0.05*A + 3.5*(Nbr+1)
    return V_flow_rate


#Combined Infiltration and Ventilation, Sensible Load

def sens_iv_load_calc_heat(Q_vi_heat,CS_air_factor,Eps_sens,Q_balhr,Q_balhr_oth,T_outdoor_heat):
    T_out = T_outdoor_heat
    Dt = 20-T_out
    cs = CS_air_factor
    Qvih = Q_vi_heat
    Qbalh = Q_balhr
    Qbal_ot = Q_balhr_oth
    eps = Eps_sens
    q_iv_sen_heating = cs * (Qvih+(1-eps)*Qbalh+Qbal_ot) * Dt
    return q_iv_sen_heating

def sens_iv_load_calc_cool(Q_vi_cool,CS_air_factor,Eps_sens,Q_balhr,Q_balhr_oth,T_outdoor_cool):
    T_out = T_outdoor_cool
    Dt = T_out-24
    cs = CS_air_factor
    Qvih = Q_vi_cool
    Qbalh = Q_balhr
    Qbal_ot = Q_balhr_oth
    eps = Eps_sens
    q_iv_sen_cool = cs * (Qvih+(1-eps)*Qbalh+Qbal_ot) * Dt
    return q_iv_sen_cool

def inf_vent_load_calc(input_data_inf_vent):
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
    Cl = input_data_inf_vent.iloc[17][0]
    Humidity_difference = input_data_inf_vent.iloc[18][0]
    Ct = input_data_inf_vent.iloc[19][0]
    Eps_tot = input_data_inf_vent.iloc[20][0]
    H_difference = input_data_inf_vent.iloc[21][0]
    
    A_eff_l_a = Leakage_Area_calc(Aes,Type_cons)   #Al = Aes* Aul
    IDF_heating = Idf_Heating_calc(H_house,Dt_heating)  #IDF
    IDF_cooling = Idf_Cooling_calc(H_house,Dt_cooling)
    I_fr_heating = inf_air_flo_rate_heat_calc(Aes,Type_cons,H_house,Dt_heating)  #Qi=Al*IDF [L/sec]    
    I_fr_cooling = inf_air_flo_rate_cool_calc(Aes,Type_cons,H_house,Dt_cooling)
    V_fr = vent_flow_rate(A_cond_floor,Nbr)
    VI_fr_heating = V_fr + I_fr_heating      #Qvent-inf=Qvent+Qinf
    VI_fr_cooling = V_fr + I_fr_cooling
    q_vi_s_heating = sens_iv_load_calc_heat(VI_fr_heating,Cs,Eps,Q_bal_fr,Q_bal_ot_fr,Dt_heating)
    q_vi_s_cooling = sens_iv_load_calc_cool(VI_fr_cooling,Cs,Eps,Q_bal_fr,Q_bal_ot_fr,Dt_cooling)
    Internal_gain = Qig_s_Calculation(A_cond_floor,Nbr)   #only cooling
    results_F = pd.read_csv("results_infvent_empty.csv",sep = ";",index_col=0)
    results_F.iloc[0][0] = A_eff_l_a
    results_F.iloc[1][0] = IDF_cooling
    results_F.iloc[2][0] = IDF_heating
    results_F.iloc[3][0] = V_fr
    results_F.iloc[4][0] = I_fr_cooling
    results_F.iloc[5][0] = I_fr_heating
    results_F.iloc[6][0] = q_vi_s_cooling
    results_F.iloc[7][0] = q_vi_s_heating
    results_F.iloc[8][0] = Internal_gain
    return results_F


#Distribution Losses

def right_table_calc(input_data_distribution):                 #one table for each column
    Table_DF_s1_l5_r0 = pd.read_csv("Table_DF_s1_l5_r0.csv",sep = ";",index_col=0)
    Table_DF_s1_l5_r0_7 = pd.read_csv("Table_DF_s1_l5_r0.7.csv",sep = ";",index_col=0)
    Table_DF_s1_l5_r1_4 = pd.read_csv("Table_DF_s1_l5_r1.4.csv",sep = ";",index_col=0)
    Table_DF_s1_l11_r0 = pd.read_csv("Table_DF_s1_l11_r0.csv",sep = ";",index_col=0)
    Table_DF_s1_l11_r0_7 = pd.read_csv("Table_DF_s1_l11_r0.7.csv",sep = ";",index_col=0)
    Table_DF_s1_l11_r1_4 = pd.read_csv("Table_DF_s1_l11_r1.4.csv",sep = ";",index_col=0)
    Table_DF_s2_l5_r0 = pd.read_csv("Table_DF_s2_l5_r0.csv",sep = ";",index_col=0)
    Table_DF_s2_l5_r0_7 = pd.read_csv("Table_DF_s2_l5_r0.7.csv",sep = ";",index_col=0)
    Table_DF_s2_l5_r1_4 = pd.read_csv("Table_DF_s2_l5_r1.4.csv",sep = ";",index_col=0)
    Table_DF_s2_l11_r0 = pd.read_csv("Table_DF_s2_l11_r0.csv",sep = ";",index_col=0)
    Table_DF_s2_l11_r0_7 = pd.read_csv("Table_DF_s2_l11_r0.7.csv",sep = ";",index_col=0)
    Table_DF_s2_l11_r1_4 = pd.read_csv("Table_DF_s2_l11_r1.4.csv",sep = ";",index_col=0)
    sum_table = [Table_DF_s1_l5_r0_7,Table_DF_s1_l5_r1_4,Table_DF_s1_l11_r0,Table_DF_s1_l11_r0_7,Table_DF_s1_l11_r1_4,Table_DF_s2_l5_r0,Table_DF_s2_l5_r0_7,Table_DF_s2_l5_r1_4,Table_DF_s2_l11_r0,Table_DF_s2_l11_r0_7,Table_DF_s2_l11_r1_4,Table_DF_s1_l5_r0,] #LIST OF tables,list of data frame 
    number_of_stories = input_data_distribution.iloc[5][0]
    leakage = input_data_distribution.iloc[2][0]      #%
    Insulation = input_data_distribution.iloc[1][0]     #R-....
    for table in sum_table:
        if number_of_stories=="1" and leakage=="5" and Insulation=="0":
            table = Table_DF_s1_l5_r0
        elif number_of_stories=="1" and leakage=="5" and Insulation=="0.7":
            table = Table_DF_s1_l5_r0_7  
        elif number_of_stories=="1" and leakage=="5" and Insulation=="1.4":
            table = Table_DF_s1_l5_r1_4
        elif number_of_stories=="1" and leakage=="11" and Insulation=="0":
            table = Table_DF_s1_l11_r0     
        elif number_of_stories=="1" and leakage=="11" and Insulation=="0.7":
            table = Table_DF_s1_l11_r0_7
        elif number_of_stories=="1" and leakage=="11" and Insulation=="1.4":
            table = Table_DF_s1_l11_r1_4
        elif number_of_stories=="2" and leakage=="5" and Insulation=="0":
            table = Table_DF_s2_l5_r0        
        elif number_of_stories=="2" and leakage=="5" and Insulation=="0.7":
            table = Table_DF_s2_l5_r0_7
        elif number_of_stories=="2" and leakage=="5" and Insulation=="1.4":
            table = Table_DF_s2_l5_r1_4
        elif number_of_stories=="2" and leakage=="11" and Insulation=="0":
            table = Table_DF_s2_l11_r0          
        elif number_of_stories=="2" and leakage=="11" and Insulation=="0.7":
            table = Table_DF_s2_l11_r0_7 
        elif number_of_stories=="2" and leakage=="11" and Insulation=="1.4":
            table =Table_DF_s2_l11_r1_4     
    return table    #find the right column

def duct_factors_calc_cooling(input_data_distribution):
    mytable = right_table_calc(input_data_distribution)                              
    Duct_loc = input_data_distribution.iloc[0][0]
    Type_cooling = input_data_distribution.iloc[3][0]
    Type_heating = input_data_distribution.iloc[4][0]
    Is_true = mytable.Conditioning_Type==Type_cooling  #  take only rows with my type cooling (C,H/F,H/P) ######################################
    myductfactor_heat = mytable[Is_true].loc[Duct_loc]["Duct_factors"]   #Duct_loc = riga,    Duct_factors= column with numerical value of typical duct loss/gain factor
    return myductfactor_heat   

def duct_factors_calc_heating(input_data_distribution):
    mytable = right_table_calc(input_data_distribution)                              
    Duct_loc = input_data_distribution.iloc[0][0]
    Type_cooling = input_data_distribution.iloc[3][0]
    Type_heating = input_data_distribution.iloc[4][0]
    Is_true = mytable.Conditioning_Type==Type_heating     
    myductfactor_cooling = mytable[Is_true].loc[Duct_loc]["Duct_factors"]
    return myductfactor_cooling

def Q_distri_Losses(input_data_distribution,Q_fenestration_heat,Q_fenestration_cool,Q_opaque_heat,Q_opaque_cool,Q_inf_vent_heat,Q_inf_vent_cool,Q_intgain):
    Q_tot_heating = Q_fenestration_heat + Q_opaque_heat + Q_inf_vent_heat
    Q_tot_cooling = Q_fenestration_cool + Q_opaque_cool + Q_inf_vent_cool + Q_intgain
    DF_cooling = duct_factors_calc_cooling(input_data_distribution) 
    DF_heating = duct_factors_calc_heating(input_data_distribution)
    Q_loss_heating = Q_tot_heating * DF_heating     #losses
    Q_loss_cooling = Q_tot_cooling * DF_cooling 
    results_F = pd.read_csv("results_distloss_empty.csv",sep = ";",index_col=0)
    results_F.iloc[0][0] = Q_loss_heating
    results_F.iloc[1][0] = Q_loss_cooling
    return results_F   #make a table with distrib. losses in summer and winter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  