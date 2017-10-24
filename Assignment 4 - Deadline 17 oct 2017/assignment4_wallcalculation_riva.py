#ASSIGNMENT 4

import os
os.chdir ("/Users/Fede/Desktop/federicoriva_as_1_2_3_4")

import assignment4_mainscript_riva as f1
 
wall_series=["wood_bevel","wood_fiberboard","gypsum_wallboard"]
wall_paraller=["glass_fiber","wood_stud"]
door=["wood_5cm"]
roof=["wood_stud","wood_5cm"]

FR=0.75 #from data

U_tot_wall=f1.wallcalc_withparaller(wall_series,wall_paraller,FR)
U_tot_door=f1.wallcalc_onlyInSeries(door)
U_tot_roof=f1.wallcalc_onlyInSeries(roof)

DT=24.8 #from data 

U_tot=[U_tot_wall,U_tot_door,U_tot_roof]

HF=[]

for anyU in U_tot:
    HF.append(anyU*DT)
    
Area_wall=105.8  #from data 
Area_door=2.2  #from data 
Area_roof=200  #from data 

Areas=[Area_wall,Area_door,Area_roof]
Q=[]

index=range(3)

for anyindex in index:
    
        Q.append(HF[anyindex]*Areas[anyindex])
  
print"Values of U are "+str(U_tot)      
                    
print"Values of HF are "+str(HF)
        
print"Values of thermal peak power loads are "+str(Q)

#pt1:wall #pt2:door #pt3:roof
        

    
    
    
    
    





