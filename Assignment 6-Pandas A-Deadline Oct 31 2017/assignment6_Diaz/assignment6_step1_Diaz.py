import pandas as pd

R1_list = ["conv",10,None,None, 0]
R2_list = ["cond",None,0.03,0.026, 0]
R3_list = ["cond",None,0.02,0.22, 0]
R4_list = ["cond",None,0.02,0.22, 0]
R5_list = ["conv",25,None,None, 0]


#Series
resistances_names_series = ["R1","R2","R3","R4","R5"]
columns_names_series=["type","h","L","k","RValue"]
area_series=0.25
ResistancesSeries_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list],index=resistances_names_series,columns=columns_names_series)
ResistancesSeries_DF["RValue"][ResistancesSeries_DF["type"]=="conv"]=1.0/(area_series*ResistancesSeries_DF["h"][ResistancesSeries_DF["type"]=="conv"])
ResistancesSeries_DF["RValue"][ResistancesSeries_DF["type"]=="cond"]=ResistancesSeries_DF["L"][ResistancesSeries_DF["type"]=="cond"]/(area_series*ResistancesSeries_DF["k"][ResistancesSeries_DF["type"]=="cond"])

Rtot_Series=ResistancesSeries_DF["RValue"].sum()

#Parallel
R6_list = [0.16,0.22,0.015,0]
R7_list = [0.16,0.72,0.22,0]
R8_list = [0.16,0.22,0.015,0]

resistances_names_parallel= ["R6","R7","R8"]
columns_names_parallel=["L","k","A","RValue"]

ResistancesParallel_DF=pd.DataFrame([R6_list,R7_list,R8_list],index=resistances_names_parallel,columns=columns_names_parallel)
ResistancesParallel_DF["RValue"]=ResistancesParallel_DF["L"]/ResistancesParallel_DF["k"]/ResistancesParallel_DF["A"]

R_Parallel=1/ResistancesParallel_DF["RValue"]
Rtot_Parallel=1/R_Parallel.sum()


Rtot_System=Rtot_Series+Rtot_Parallel


print("The total resistance of the system is "+ str(Rtot_System)+" m^2C/W")

heightw=3
widthw=5
Tin=20
Tout=-10
Awall=heightw*widthw
Aunit=0.25*1


Qunit=(Tin-Tout)/Rtot_System
Qtot=Qunit*(Awall/Aunit)

print("\n")
print (  "The rate of heat transfer through the wall is  " + str (Qtot)+ " W" )