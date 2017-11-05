
#--------------------------ASSIGNMENT 6--------------------------------------
# -------------------------Using Pandas------------------------------------

# Name : Hendra Suryana Putra

# Heat loss through a composite wall

# Thermal Conductivity and Convection Heat Transfer on Example D

import pandas as pd


# Resistance in Series

R_names_ser = ["Rconv1","Rp1","Rf","Rp2","Rconv2"]
columns_names_ser = ["type","h","L","k","RValue"]

Rconv1_list = ["conv",10,None,None,0]
Rp1_list = ["cond",None,0.02,0.22,0]
Rf_list = ["cond",None,0.03,0.026,0] 
Rp2_list = ["cond",None,0.02,0.22,0]
Rconv2_list = ["conv",25,None,None,0]

Resistances_DF = pd.DataFrame([Rconv1_list,Rp1_list,Rf_list,Rp2_list,Rconv2_list],
index = R_names_ser, columns = columns_names_ser )

Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1.0/Resistances_DF["h"][Resistances_DF["type"]=="conv"]
Resistances_DF["RValue"][Resistances_DF["type"]=="cond"]=Resistances_DF["L"][Resistances_DF["type"]=="cond"] / Resistances_DF["k"][Resistances_DF["type"]=="cond"]

R_Rtot_Ser = sum(Resistances_DF["RValue"])

R_A = 0.25
Rtot_ser = R_Rtot_Ser/R_A

print "The Total Resistance in Series is " + str(Rtot_ser) + " (degC/W)"
print "------------------------------------------------------------------"


# Resistance in Parallel

R_names_par = ["Rpp1","Rb","Rpp2"]
columns_names_par = ["type","k","A","RValue"]

Rpp1_list = ["cond",0.22,0.015,0]
Rb_list = ["cond",0.72,0.22,0]
Rpp2_list = ["cond",0.22,0.015,0]

Resistances_DF = pd.DataFrame([Rpp1_list,Rb_list,Rpp2_list],
index = R_names_par, columns = columns_names_par )

Resistances_DF["RValue"] = (Resistances_DF["A"] * Resistances_DF["k"])

R_Lp = 0.16
R_Rtot_Par = sum(Resistances_DF["RValue"])

Rtot_Par = R_Lp/R_Rtot_Par

print "The Total Resistance in Parallel is " + str(Rtot_Par) + " (degC/W)"
print "------------------------------------------------------------------"


# Resistance of the wall

Rtotal = Rtot_ser+Rtot_Par

print "Thus, The overall resistance of the wall is " + str(Rtotal) + " (degC/W)"


#---------------------------------------------------------------------------

# Temperature

Tin = 20
Tout = -10

DT=Tin-Tout

#---------------------------------------------------------------------------

# Heat transfer Rate

Qtot=DT/Rtotal

print "------------------------------------------------------------------"
print "------------------------------------------------------------------"
print "Thus, The Heat Transfer Rate through the system is " +str(Qtot)+ "(W)"

