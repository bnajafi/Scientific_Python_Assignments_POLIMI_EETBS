# Energy And Environmental Technologies For Building Systems : Assignment 03, Step-1

# Submitted By : Danish Ahmad Mir

# Assignment Based On Exercise-1 From Topic 1.3 (Determine the overall unit thermal resistance and the overall heat transfer coefficient)

#Definitions Used :

# stud_layer is the layer through the stud (without any insulation layer)

# fstud : the fraction of stud area compared to overall area

# Ustud : heat transfer coefficient of stud

# ins_layer is the layer through the insulation (without any stud layer)

# conv_layer is the layer of air in the inside and outside of the wall

# fins : the fraction of insulation area compared to overall area

# Uins : heat transfer coefficient of insulation

# Tin : Inside temperature of the wall

# Tout : Outside temperature of the wall

# Awall : The total area of the wall

# Qtot : The total heat transfer of the wall

material_table = {"outsideSurface":0.03,"woodBevelLappedSliding_13mm_200mm":0.14,
"woodFiberboard_13mm":0.23,"glassFiberIns_90mm":2.52,"woodStud_38mm_90mm":0.63,
"gypsumWallboard_13mm":0.079,"insideSurface":0.12}

conv_layer = ["outsideSurface","insideSurface"]

# Step-A : Calculate the total Resistance Value on Stud Layer

stud_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"woodStud_38mm_90mm","gypsumWallboard_13mm"]

stud_layer_tot = stud_layer + conv_layer

Rtot_stud = 0
Rvalue_stud_loop = []

for Rstud in stud_layer_tot:
    Rvalue_stud = material_table[Rstud]
    Rtot_stud = Rtot_stud + Rvalue_stud
    Rvalue_stud_loop.append(Rvalue_stud)
  
print "The value of each resistance in stud layer is " + str(Rvalue_stud_loop)  
print "Total Resistance in stud layer is " + str(Rtot_stud) + " (m^2 DegC/W)"
print "*********************************************************"

# Step-B : Calculate the total Resistance Value on Insulation Layer

ins_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"glassFiberIns_90mm","gypsumWallboard_13mm"]

ins_layer_tot = ins_layer + conv_layer

Rtot_ins = 0
Rvalue_ins_loop = []

for Rins in ins_layer_tot:
    Rvalue_ins = material_table[Rins]
    Rtot_ins = Rtot_ins + Rvalue_ins
    Rvalue_ins_loop.append(Rvalue_ins)
    
print "The value of each resistance in insulation layer is " + str(Rvalue_ins_loop)
print "Total Resistance in insulation layer is " + str(Rtot_ins) + " (m^2 DegC/W)"
print "*********************************************************"

# Step-C : Calculate the Overall heat transfer coefficient (U) factor of stud

Ustud = 1/Rtot_stud
fstud = 0.25
Ustud_tot = fstud*Ustud

print "The total heat transfer coefficient on stud with 0.25 fraction area is " + str(Ustud_tot) + " (W/m^2 deg C)"
print "*********************************************************"

# Step-D : Calculate the Overall heat transfer coefficient (U) factor of insulation

Uins = 1/Rtot_ins
fins = 0.75
Uins_tot = fins*Uins

print "The total heat transfer coefficient on insulation with 0.75 fraction area is " + str(Uins_tot) + " (W/m^2 deg C)"
print "*********************************************************"

# Step-E : Calculate the Overall heat transfer coefficient (U) Total of the wall

Utot = Ustud_tot + Uins_tot

print "Thus, the overall heat transfer coefficient of the wall is " + str(Utot) + " (W/m^2 deg C)"
print "*********************************************************"


# Step-F : Calculate the total rate of heat transfer of the wall

# Temperature

Tin = 22
Tout = -2

DT=Tin-Tout

print "The differential temperature between inside and outside of the wall is " + str(DT) + " (Deg C)"
print "*********************************************************"

# Step-G : Area of the wall

Atot = 50*2.5
Awall = 0.8*Atot

print "The total area of the wall is " + str(Awall) + " (m^2)"
print "*********************************************************"

# Step-H : Calculation for Q total

Q = Utot*Awall*DT

# change from Watt to KWatt

Qtot = Q/1000

print "Thus, the total heat transfer rate of the wall is " + str(Qtot) + " (kW)"
