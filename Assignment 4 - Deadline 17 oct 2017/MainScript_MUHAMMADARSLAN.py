# 16/10/17

#  ----------------Assignment-4--Part-2--------------------

#  ---Example (Calculation of Heat factor & Heat load)------------

# ------------------MUHAMMAD ARSLAN--------------------

#-------------------Using Import Function ----------------------------------------------------------#


import os
os.chdir("C:\Users\arslan\Desktop\Assignment4")  #Adress for Calling function from first file
import WallCalculation_MUHAMMADARSLAN as A

#----Defining all values----

layers_In_series=["Wood bevel","Gypsum wallboard","insideSurface","OutsideSurfaceWinter"]
layers_In_parallel=["Glass fiber insulation","Wood stud"]
layers_for_Roof=["insideSurface","outsideSurfaceWinter","Wood","Asphalt shingle roofing"]
layers_for_Door=["insideSurface","outsideSurfaceWinter","Wood"]

D_T= (25)                                                  #Change in temp: in deg C
W_Area,R_Area,D_Area=105.8,200,2.2                         #Areas in m^2
 
#----Getting the U-values from imported functions of First File----

Uwall=A.wallCalc_LIS()
Udoor=A.wallCalc_DR()["U-Value of Door"]
Uroof=A.wallCalc_DR()["U-value of Roof"]

#----Calculating the Heating factor from given data----

HFwall= ((Uwall)*(D_T))          #Heating factor for wall
HFdoor= ((Udoor)*(D_T))          #Heating factor for door 
HFroof= ((Uroof)*(D_T))          #Heating factor for roof

#----Calculating the Heating load-------

QHwall= ((HFwall)*(W_Area))      #Heating load for wall
QHdoor= ((HFdoor)*(D_Area))      #Heating load for door 
QHroof= ((HFroof)*(R_Area))      #Heating load for roof

HeatLoad_total= ((QHwall)+(QHdoor)+(QHroof))

print("\nThe total heating load is: "+str(HeatLoad_total)+" Watt")