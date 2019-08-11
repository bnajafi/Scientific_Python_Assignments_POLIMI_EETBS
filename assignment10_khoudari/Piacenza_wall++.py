import os
os.chdir("D:/Polimi Piacenza/Energy and Environment/notes/3 Python Files and Guidelines/assignment10_khoudari")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

import fenestration_functions as func
import IntGains_Inf_Vent_DistrLosses as iv
import FunctionsOpaque as funcOp
import psySI as SI
import latent_functions as lat
#Weather Inputs:

inputs_DF = pd.read_csv("input_weather_Piacenza.csv",sep=";",index_col=0)
inputs_list = func.weather_data_calculator(inputs_DF)


# Opaque surfaces Calculation:
numericalDataDF = pd.read_csv("input_numerical_data.csv",sep=";",index_col= 0)
dataDF = pd.read_csv("input_data.csv",sep=";",index_col= 0)
materials_DataFrame = pd.read_csv("resistences_materials.csv",sep=";",index_col= 1)
inputWalls_DataFrame_winter = pd.read_csv("input_data_walls_winter++.csv",sep=";",index_col= 0)
inputWalls_DataFrame_summer = pd.read_csv("input_data_walls_summer++.csv",sep=";",index_col= 0)
inputDoor_DataFrame_winter = pd.read_csv("input_data_door_winter.csv",sep=";",index_col= 0)
inputDoor_DataFrame_summer = pd.read_csv("input_data_door_summer.csv",sep=";",index_col= 0)
    
U_wall_winter = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_winter,materials_DataFrame)  
U_wall_summer = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_summer,materials_DataFrame)  
U_door_winter = funcOp.Utot_door_Calculator(inputDoor_DataFrame_winter,materials_DataFrame)  
U_door_summer = funcOp.Utot_door_Calculator(inputDoor_DataFrame_summer,materials_DataFrame)  

print "\nThis is the value of Uwall_winter: " + str(U_wall_winter) + "  W/(m^2 * K)"
print "This is the value of Udoor_winter: " + str(U_door_winter)+ "  W/(m^2 * K)"
print "This is the value of Uceiling: " + str(numericalDataDF["value"]["U_ceiling"]) + "  W/(m^2 * K)"
QtotOpaque_winter = funcOp.QtotOpaque_winter_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_winter,numericalDataDF["value"]["U_ceiling"],U_door_winter,inputs_list["deltaTheating"])
print "\tThis is the opaque heating load: " + str(QtotOpaque_winter) + " W\n"

print "\nThis is the value of Uwall_summer: " + str(U_wall_summer) + "  W/(m^2 * K)"
print "This is the value of Udoor_summer: " + str(U_door_summer)+ "  W/(m^2 * K)"
print "This is the value of Uceiling: " + str(numericalDataDF["value"]["U_ceiling"]) + "  W/(m^2 * K)"
QtotOpaque_summer=funcOp.QtotOpaque_summer_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_summer,numericalDataDF["value"]["U_ceiling"],U_door_summer,dataDF["characteristic"]["colour_roof"],dataDF["characteristic"]["material_roof"],inputs_list["deltaTcooling"],inputs_list["DRcooling"],dataDF["characteristic"]["walls_surface_type"],dataDF["characteristic"]["ceiling_surface_type"],dataDF["characteristic"]["doors_surface_type"])
print "\tThis is the opaque cooling load: " + str(QtotOpaque_summer) + " W\n"


#Fenestration surfaces Calculation:
windows_DF = pd.read_csv("input_fenestration.csv",sep=";",index_col=0)
windows_DF["Area"] = windows_DF["Height"]*windows_DF["Width"]

Qfen_heating_load = func.Qfen_heating_calculator(windows_DF,inputs_list)
print 'The total amount of the heating load for the windows is '+str(Qfen_heating_load)+' W.'
Qfen_cooling_load = func.Qfen_cooling_calculator(windows_DF,inputs_list)
print 'The total amount of the cooling load for the windows is '+str(Qfen_cooling_load)+' W.'
#windows_DF.to_csv("results_fenestration.csv",sep =";")


#Infiltration, Ventilation and Distribution losses Calculation:
input_data_inf_vent = pd.read_csv("input_inf_vent.csv",sep = ";",index_col=0)
Output_Inf_Vent = iv.inf_vent_load_calc(input_data_inf_vent)

input_data_distribution = pd.read_csv("Input_distribution.csv",sep = ";",index_col=0)
Losses = iv.Q_distri_Losses(input_data_distribution,Qfen_heating_load,Qfen_cooling_load,QtotOpaque_winter,QtotOpaque_summer,Output_Inf_Vent.iloc[7][0],Output_Inf_Vent.iloc[6][0],Output_Inf_Vent.iloc[8][0])

#Latent results
QtotLatent = lat.Qtot_latent (input_data_inf_vent, inputs_list)

#Final Results
results_DF = pd.read_csv("results_empty.csv",sep=";",index_col=0)
results_DF["Heating"] = [QtotOpaque_winter,Qfen_heating_load,0,0,Output_Inf_Vent.iloc[7][0],Losses.iloc[0][0],0,0]
results_DF["Cooling"] = [QtotOpaque_summer,Qfen_cooling_load,0,Output_Inf_Vent.iloc[8][0],Output_Inf_Vent.iloc[6][0],Losses.iloc[1][0],0,QtotLatent]
for column in results_DF.columns.tolist():
    sensible_loads = pd.Series(results_DF[column][0:6])
    results_DF[column]["Q_sensible_tot"] = sensible_loads.sum()
#results_DF.to_csv("results_wholeRFL.csv",sep =";")
    
 
    
    
print "\nThis is the value of sensible internal gain: "+str(Output_Inf_Vent["Results"]["Internal Gain, sensible [W]"])+" W."
print "This is the value of sensible infiltration-ventilation Cooling load: "+str(Output_Inf_Vent["Results"]["Sensible Infiltration/Ventilation Cooling Load [W]"])+" W."
print "This is the value of sensible infiltration-ventilation Heating load: "+str(Output_Inf_Vent["Results"]["Sensible Infiltration/Ventilation Heating Load [W]"])+" W.\n"    
print "This is the value of Heating distribution losses: "+str(Losses["Results"]["Heating distribution losses"])+" W."
print "This is the value of Cooling distribution losses: "+str(Losses["Results"]["Cooling distribution losses"])+" W.\n" 
print "\t\t\t So the total Sensible Heating Load is :"+str(results_DF["Heating"]["Q_sensible_tot"])+" W."      
print "\t\t\t So the total Sensible Cooling Load is :"+str(results_DF["Cooling"]["Q_sensible_tot"])+" W.\n"      
print "Here is given a table with all the results:\n"
print results_DF   
    

