# -*- coding: utf-8 -*-
#      Assigment 9 Calculation of the Heating and cooling loads of the opaques surfaces

print """        Assigment 9 Calculation of the Heating and cooling loads of the opaques surfaces\n"""

#  import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

material={"Inside_surface":0.12,"Winter": 0.030,"Summer": 0.044,"Common brick":0.12,
"Wood_bevel_lapped_siding": 0.14,"Wood_fiberboard_sheeting":0.23,
"Glass_fiber_insulation":2.52,"Wood stud":0.63,"Gypsum wallboard":0.079,"Wood":0.44,"air_gap":0.62}

# List of materials in series configuration

ListSWall=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting","Common brick",
"Glass_fiber_insulation","Gypsum wallboard"]

# List of materials in parallel configuration

ListPWall=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting","Common brick",
"Wood stud","Gypsum wallboard"]

ListDoor=["Wood"]
# Areas


# Declaration of the function for calculate the U factor value for summer [0] and winter [1]
# according with the list of materials in series
def Uvalue(List):
    
    # Adding the thermal resistance for the inside and outside surface
    airofboth=["Inside_surface","Winter"]
    # Defining the total list of materials in series 
    Layers=List+airofboth
    # Defining the variables for the total unit thermal resistance 
    Rtotal=0   
    # Defining the for cycle to acquired and compute the unit thermal resistance for a 
    # specific material in the list of materials 
    
    for anylayer in Layers:
        # Acquiring the thermal resistance for the specific material of the list in [m2*ºC/W]
        Rvalue_layer=material[anylayer]
        # Computing the sum of each unit thermal resistance of each material in series in [m2*ºC/W]
        Rtotal=Rtotal+Rvalue_layer
    UvalueWinter=1/(Rtotal)
    UvalueSummer=1/(Rtotal+0.014)
    return np.array([UvalueSummer,UvalueWinter])
    
# Declaration of the function for calculate the heating load of the opaque surface
    
def heating(ufactor,area):
    #Delta of temperature in winter
    DTwinter=24.8
    #Calulation of the Heating factor
    HF=ufactor*DTwinter
    #Calculation of the Heating load
    Q=area*HF
    #Return Heating factor [0] and Heating load [1]
    return np.array([HF,Q])
    
def cooling(ufactor,area,cf):
    #Calculation of the Cooling factor
    CF=ufactor*cf
    #Calculation of the Cooling load
    Q=area*CF
    #Return Cooling factor [0] and Cooling load [1]
    return np.array([CF,Q])  

#Calculations of the Ufactor of each opaque surface
#Door 
UDoor=Uvalue(ListDoor) 
#Wall assuming that 70% wood and 30% insulation
wallSeries=Uvalue(ListSWall)
wallParallel=Uvalue(ListPWall)
Uwall=(wallSeries*0.7)+(wallParallel*0.3)
#ceiling
Uceiling=0.25

#Calculations of the Heating and Cooling load of each opaque surface
#Door assuming that Area = 2.2 m^2 and (CF/U)= 11.815
QHdoor=heating(UDoor[1],2.2)
QCdoor=cooling(UDoor[0],2.2,11.815)
#Wall assuming that Area = 105.8 m^2 and (CF/U)= 11.815
QHwall=heating(Uwall[1],105.8)
QCwall=cooling(Uwall[0],105.8,11.815)
#Ceiling assuming that Area = 200 m^2 and (HF/U)= 10.292
QHceiling=heating(Uceiling,200)
QCceiling=cooling(Uceiling,200,10.292)

#Creation of the 2D array with the Heating and cooling load of each opaque surface
#index
OpaqueLoadrows=["Wall","Ceiling","Door"]
#columns
OpaqueLoadColumns=["Area", "Uheating", "HF", "Qheating", "Ucooling", "CF", "Qcooling"]
#Row in the following order Area, Uheating, HF, Qheating, Ucooling, CF, Qcooling
wall=[105.8,Uwall[1],QHwall[0],QHwall[1],Uwall[0],QCwall[0],QCwall[1]]
door=[2.2,UDoor[1],QHdoor[0],QHdoor[1],UDoor[0],QCdoor[0],QCdoor[1]]
ceiling=[200,Uceiling,QHceiling[0],QHceiling[1],Uceiling,QCceiling[0],QCceiling[1]]
#Definition of the 2D array
Opaque=pd.DataFrame([wall,ceiling,door],index=OpaqueLoadrows,columns=OpaqueLoadColumns)

#ploting Heating and Cooling load of the opaque surfaces

#closing previous plots
plt.close("all")
y=Opaque["Qheating"].tolist()
x=Opaque["Qcooling"].tolist()
#Heating
fig1=plt.figure()
plt.pie(y,labels=OpaqueLoadrows,startangle=90,explode=(0.025,0.025,0.025),autopct='%1.1f%%')
plt.legend()
plt.title("Heating load of opaque surfaces")
plt.show()
#Cooling
fig2=plt.figure()
plt.pie(x,labels=OpaqueLoadrows,startangle=90,explode=(0.025,0.025,0.025),autopct='%1.1f%%')
plt.legend()
plt.title("Cooling load of opaque surfaces")
plt.show()

#Modifying the U facotr of the wall

#list of the new materials of the wall
ListNewWall=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting","Common brick",
"air_gap","Gypsum wallboard","Glass_fiber_insulation"]

#Calculating the U factor of the new wall
NewWall=Uvalue(ListNewWall)
#Wall assuming that Area = 105.8 m^2 and (CF/U)= 11.815
QHwallnew=heating(NewWall[1],105.8)
QCwallnew=cooling(NewWall[0],105.8,11.815)
#Calculating the Overall heating load without the new wall
heating1=Opaque["Qheating"].sum()
#Calculating the new Overall heating load with the new wall
heating2=heating1-Opaque["Qheating"]["Wall"]+QHwallnew[1]

#ploting the two Overall heating load 
fig3=plt.figure()
items=[1,2]
Overall=[heating1,heating2]
color=["b","r"]
labels=["Assigned wall""\n""U="+str(QHwall[1]),"Modified wall""\n""U="+str(QHwallnew[1])]
plt.bar(items,Overall,color=color)
plt.xticks(items,labels)
plt.title("Overall Heating load for each U factor of the wall")
plt.xlabel("U factor (W/m^2*K)")
plt.ylabel("Watts (W)")
plt.show()