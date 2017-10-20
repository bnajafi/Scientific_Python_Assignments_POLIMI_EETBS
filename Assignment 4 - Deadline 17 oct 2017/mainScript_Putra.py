#------------------------------Assignment 4------------------------------------
#--------------------------Hendra Suryana Putra--------------------------------


import os
os.chdir("/Users/hendrasuryanaputra/Dropbox/Python4ScientificComputing_Fundamentals/Assignment_4") # if shit happens, replace \ to / 

import WallCalculation_Putra as FC

#--------------------------------Calculation for Wall---------------------------

# Input for Stud Layer
print "This is the calculation for WALL LAYER that consist of"
print "-------------------------------------------------------------------------------------"
print "Stud layer"

stud_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"woodStud_38mm_90mm","gypsumWallboard_13mm"]
    
Rtot_stud = FC.wallCalc_withParallel(stud_layer)

# Calculate the U factor of stud ----------------------------------------------

Ustud = 1/Rtot_stud["R total"]
fstud = 0.25
Ustud_tot = fstud*Ustud

print "The total heat transfer coefficient on stud is " + str(Ustud) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on stud with 0.25 fraction area is " + str(Ustud_tot) + " (W/m^2 deg C)"
print "-------------------------------------------------------------------------------------"

# Input for Insulation Layer

print "Insulation layer"
ins_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"glassFiberIns_90mm","gypsumWallboard_13mm"]

Rtot_ins = FC.wallCalc_withParallel(ins_layer)
    
# Calculate the U factor of insulation ----------------------------------------------

Uins = 1/Rtot_ins["R total"]
fins = 0.75
Uins_tot = fins*Uins

print "The total heat transfer coefficient on insulation is " + str(Uins) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on insulation with 0.75 fraction area is " + str(Uins_tot) + " (W/m^2 deg C)"
print "-------------------------------------------------------------------------------------"


# Calculate the U Total of the wall ----------------------------------------------------

Uwall = Ustud_tot + Uins_tot

print "Thus, the overall heat transfer coefficient of the wall is " + str(Uwall) + " (W/m^2 deg C)"
print "-------------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------------"



#------------------------Calculation for Door and Ceiling-------------------------


# Input for Door Layer

print "This is the calculation for DOOR LAYER"

door_layer = ["wood_50mm"]
Rtot_door = FC.wallCalc_withSeries(door_layer)

# Calculate the U factor of Door ----------------------------------------------

Udoor = 1/Rtot_door["R total"]

print "The total heat transfer coefficient on Door is " + str(Udoor) + " (W/m^2 deg C)"
print "-------------------------------------------------------------------------------------"

# Input for Ceiling Layer

print "This is the calculation for CEILING LAYER"

ceiling_layer = ["Asphalt_Shingle_Roofing","wood_100mm","Acoustic_Tile","ConcreteBlockLightWeight_439mm"]  
Rtot_ceiling = FC.wallCalc_withSeries(ceiling_layer)

# Calculate the U factor of Ceiling ----------------------------------------------

Uceiling = 1/Rtot_ceiling["R total"]

print "The total heat transfer coefficient on Ceiling is " + str(Uceiling) + " (W/m^2 deg C)"
print "-------------------------------------------------------------------------------------"



#-----------------------------Heating Factor------------------

Tht = -4.8
Tint = 20

DT = Tint-Tht

print "The Differential Temperature is " + str(DT) + " (Deg C)"

HF_wall = Uwall*DT
HF_door = Udoor*DT
HF_Ceiling = Uceiling*DT

print "Heat factor for Wall is " + str(HF_wall) + " (W/m^2)"
print "Heat factor for Door is " + str(HF_door) + " (W/m^2)"
print "Heat factor for Ceiling is " + str(HF_Ceiling) + " (W/m^2)"


#-----------------------------Total Load------------------

A_wall = 105.8
A_door = 2.2
A_Ceiling = 200

Qwall = HF_wall*A_wall
Qdoor = HF_door*A_door
QCeiling = HF_Ceiling*A_Ceiling

print "Heating load for Wall is " + str(Qwall) + " W"
print "Heating load for Door is " + str(Qdoor) + " W"
print "Heating load for Ceiling is " + str(QCeiling) + " W"

Qtotal = Qwall+Qdoor+QCeiling

Qtotal_kW = Qtotal/1000
print "-------------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------------"

print "Thus, the total heating load for opaque surface (wall, door, and ceiling) is " + str(Qtotal_kW) + " kW"