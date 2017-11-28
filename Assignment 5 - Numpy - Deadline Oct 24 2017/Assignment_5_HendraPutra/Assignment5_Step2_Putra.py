#------------------------Assignment 5 Step 2------------------------------

# Name : Hendra Suryana Putra

#Definition
# stud_layer is the layer through the stud (without any insulation layer)
# ins_layer is the layer through the insulation (without any stud layer)
# conv_layer is the layer of air in the inside and outside of the wall
# fstud : the fraction of stud area compared to overall area
# fins : the fraction of insulation area compared to overall area
# Ustud : heat transfer coefficient of stud
# Uins : heat transfer coefficient of insulation
# Tin : Inside temperature of the wall
# Tout : Outside temperature of the wall
# Awall : The total area of the wall
# Qtot : The total heat transfer of the wall

import numpy as np

mat_names = np.array(["outsideSurface","woodBevelLappedSliding_13mm_200mm",
"woodFiberboard_13mm","glassFiberIns_90mm","woodStud_38mm_90mm",
"gypsumWallboard_13mm","insideSurface"])

mat_values = np.array([0.03,0.14,0.23,2.52,0.63,0.079,0.12])

# Stud Layer

stud_layer = np.array(["outsideSurface","woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"woodStud_38mm_90mm","gypsumWallboard_13mm","insideSurface"])

RValue = np.zeros(stud_layer.size)

for Rstud in stud_layer:
    RValue[stud_layer==Rstud] = mat_values[mat_names==Rstud]

Rtot_stud = RValue.sum()


print "Total Resistance in stud layer is " + str(Rtot_stud) + " (m^2 DegC/W)"
print "-----------------------------------------------------------------------------"

# Insulation Layer

ins_layer = np.array (["outsideSurface","woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"glassFiberIns_90mm","gypsumWallboard_13mm","insideSurface"])

RValue1 = np.zeros(ins_layer.size)

for Rins in ins_layer:
    RValue1[ins_layer==Rins] = mat_values[mat_names==Rins]

Rtot_ins = RValue1.sum()

print "Total Resistance in insulation layer is " + str(Rtot_ins) + " (m^2 DegC/W)"
print "-----------------------------------------------------------------------------"

# Calculate the U factor of stud ----------------------------------------------

Ustud = 1/Rtot_stud
fstud = 0.25
Ustud_tot = fstud*Ustud

print "The total heat transfer coefficient on stud with 0.25 fraction area is " + str(Ustud_tot) + " (W/m^2 deg C)"

    
# Calculate the U factor of insulation ----------------------------------------------

Uins = 1/Rtot_ins
fins = 0.75
Uins_tot = fins*Uins

print "The total heat transfer coefficient on insulation with 0.75 fraction area is " + str(Uins_tot) + " (W/m^2 deg C)"


# Calculate the U Total of the wall ----------------------------------------------------

Utot = Ustud_tot + Uins_tot

print "Thus, the overall heat transfer coefficient of the wall is " + str(Utot) + " (W/m^2 deg C)"
print "-----------------------------------------------------------------------------"


# Calculate the total rate of heat transfer of the wall

# Temperature

Tin = 22
Tout = -2

DT=Tin-Tout

print "The differential temperature between inside and outside of the wall is " + str(DT) + " (Deg C)"

# Area of the wall

Atot = 50*2.5
Awall = 0.8*Atot

print "The total area of the wall is " + str(Awall) + " (m^2)"
print "-----------------------------------------------------------------------------"
print "-----------------------------------------------------------------------------"

# Q total

Q = Utot*Awall*DT

# change from Watt to KWatt

Qtot = Q/1000

print "Thus, the total heat transfer rate of the wall is " + str(Qtot) + " (kW)"