#Using pandas for resistance calculations
import pandas as pd

A_wall = 15   #area of wall [m^2]
A_unit = 0.25     #unit area ((H_brick+T_p2*2)*W_wall) 
T_1 = 20 #indoor temperature
T_2 = -10 #outdoor temperature

columns_names = ["type","h","L","k","RValue"]

#For layers in series
RSeries_names=["R_outside","R_foam","R_plaster1","R_plaster2","R_inside"]
R1_list = ["conv",10,None,None,0]
R2_list = ["cond",None,0.03,0.026,0]
R3_list = ["cond",None,0.02,0.22,0]
R4_list = ["cond",None,0.02,0.22,0]
R5_list = ["conv",25,None,None, 0] 

Resistances_Series = pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list], index = RSeries_names, columns=columns_names)
#Resistances_Series["RValue"][Resistances_Series["type"]=="conv"] = 1.0/Resistances_Series["h"][Resistances_Series["type"]=="conv"] # Calc R values of conv R=1/h
#Resistances_Series["RValue"][Resistances_Series["type"]=="cond"] = Resistances_Series["L"][Resistances_Series["type"]=="cond"] /Resistances_Series["k"][Resistances_Series["type"]=="cond"] # Calc R values of conv R=L/k
R_conv = 1.0/Resistances_Series["h"][Resistances_Series["type"]=="conv"]
R_cond = Resistances_Series["L"][Resistances_Series["type"]=="cond"] /Resistances_Series["k"][Resistances_Series["type"]=="cond"] 
Rtot = sum(R_conv)+sum(R_cond)
Rtot_Series = Rtot/A_unit  #Total resistance for series layers

#For Layers in Parallel:
RParallel_names=["R_plaster","R_brick","R_plaster"] 
R6_list = ["cond",0.015,0.16,0.22,0]
R7_list = ["cond",0.22,0.16,0.72,0]
R8_list = ["cond",0.015,0.16,0.22,0]

Resistances_Parallel = pd.DataFrame([R6_list,R7_list,R8_list], index = RParallel_names, columns=columns_names)
RValues_parallel=1/(Resistances_Parallel["L"][Resistances_Parallel["type"]=="cond"] /(Resistances_Parallel["k"]
                 [Resistances_Parallel["type"]=="cond"]*Resistances_Parallel["h"][Resistances_Parallel["type"]=="cond"]))
Rtot_parallel = 1/sum(RValues_parallel) #Total resistance for parallel layers

#Total resistance
R_tot = round(Rtot_Series+Rtot_parallel,4)

# Heat transfer
Q_unit = (T_1 - T_2) / R_tot #total heat transfer through the wall per unit width [W]
Q_wall = round(Q_unit * (A_wall/A_unit),4) #total heat transfer through the wall [W]

print 'The total thermal resistance is '+str(R_tot)+ ' degC/W'
print 'The rate of heat transfer through the wall is '+str(Q_wall)+ ' W'
print '*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'