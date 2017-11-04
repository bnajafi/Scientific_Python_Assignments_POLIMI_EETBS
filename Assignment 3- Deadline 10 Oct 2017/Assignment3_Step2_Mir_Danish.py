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

def wall_calc(defineYourLayer):

    material_table = {"outsideSurface":0.03,"woodBevelLappedSliding_13mm_200mm":0.14,
    "woodFiberboard_13mm":0.23,"glassFiberIns_90mm":2.52,"woodStud_38mm_90mm":0.63,
    "gypsumWallboard_13mm":0.079,"insideSurface":0.12}
    
    conv_layer = ["outsideSurface","insideSurface"]
    
# Step-A : Calculate the total Resistance Value 
    
    yourNewLayer = defineYourLayer + conv_layer
    
    print "The layer consist of " + str(defineYourLayer)
    
    Rtotal = 0
    Rvalue_NewLayer = []
    
    for RNewLayer in yourNewLayer:
        Rvalue_new = material_table[RNewLayer]
        Rtotal = Rtotal + Rvalue_new
        Rvalue_NewLayer.append(Rvalue_new)
        
    print "Total Resistance in this layer is " + str(Rtotal) + " (m^2 DegC/W)"
    result = {"R total":Rtotal,"All R value of New Layer":Rvalue_NewLayer}
# print result  
    return result

# Input for Stud Layer

print "This is the calculation for stud layer"
stud_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"woodStud_38mm_90mm","gypsumWallboard_13mm"]
    
Rtot_stud = wall_calc(stud_layer)

# Step-B : Calculate the Overall heat transfer coefficient (U) factor of stud

Ustud = 1/Rtot_stud["R total"]
fstud = 0.25
Ustud_tot = fstud*Ustud

print "The total heat transfer coefficient on stud is " + str(Ustud) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on stud with 0.25 fraction area is " + str(Ustud_tot) + " (W/m^2 deg C)"
print "*********************************************************"

# Input for Insulation Layer

print "This is the calculation for insulation layer"
ins_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"glassFiberIns_90mm","gypsumWallboard_13mm"]

Rtot_ins = wall_calc(ins_layer)
    
# Step-C : Calculate the Overall heat transfer coefficient (U) factor of insulation

Uins = 1/Rtot_ins["R total"]
fins = 0.75
Uins_tot = fins*Uins

print "The total heat transfer coefficient on insulation is " + str(Uins) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on insulation with 0.75 fraction area is " + str(Uins_tot) + " (W/m^2 deg C)"
print "*********************************************************"


# Step-D : Calculate the Overall heat transfer coefficient (U) Total of the wall

Utot = Ustud_tot + Uins_tot

print "Thus, the overall heat transfer coefficient of the wall is " + str(Utot) + " (W/m^2 deg C)"
print "*********************************************************"


# Step-E : Calculate the total rate of heat transfer of the wall

# Temperature

Tin = 22
Tout = -2

DT=Tin-Tout

print "The differential temperature between inside and outside of the wall is " + str(DT) + " (Deg C)"

# Area of the wall

Atot = 50*2.5
Awall = 0.8*Atot

print "The total area of the wall is " + str(Awall) + " (m^2)"
print "*********************************************************"

# Q total

Q = Utot*Awall*DT

# change from Watt to KWatt

Qtot = Q/1000

print "Thus, the total heat transfer rate of the wall is " + str(Qtot) + " (kW)"