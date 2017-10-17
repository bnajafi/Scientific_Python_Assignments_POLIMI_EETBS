# Assignment 3 step 2 _10oct17.


def wall_calc(define_a_Layer):

    material_table = {"outsideSurface":0.03,"woodBevelLappedSliding_13mm_200mm":0.14,
    "woodFiberboard_13mm":0.23,"glassFiberIns_90mm":2.52,"woodStud_38mm_90mm":0.63,
    "gypsumWallboard_13mm":0.079,"insideSurface":0.12}
    
    conv_layer = ["outsideSurface","insideSurface"]
    
    # Calculate the total Resistance Value 
    
    yourNewLayer = define_a_Layer + conv_layer
    print "The layer consist of " + str(define_a_Layer)
    
    Rtotal = 0
    Rvalue_NewLayer = []
    
    for RNewLayer in yourNewLayer:
        Rvalue_new = material_table[RNewLayer]
        Rtotal = Rtotal + Rvalue_new
        Rvalue_NewLayer.append(Rvalue_new)
        
    print "Total Resistance in this layer is " + str(Rtotal) + " (m^2 DegC/W)"
    result = {"R total":Rtotal,"All R value of New Layer":Rvalue_NewLayer}
    return result

# Input for Stud Layer
print "This is the calculation for stud layer"
stud_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"woodStud_38mm_90mm","gypsumWallboard_13mm"]    
Rtot_stud = wall_calc(stud_layer)

# Calculate the U factor of stud

Ustud = 1/Rtot_stud["R total"]
fstud = 0.25
Ustud_tot = fstud*Ustud
print "The total heat transfer coefficient on stud is " + str(Ustud) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on stud with 0.25 fraction area is " + str(Ustud_tot) + " (W/m^2 deg C)"
print "*************************"

#  for Insulation Layer

print "This is the calculation for insulation layer"
ins_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"glassFiberIns_90mm","gypsumWallboard_13mm"]

Rtot_ins = wall_calc(ins_layer)
    
# Calculate the U factor of insulation
Uins = 1/Rtot_ins["R total"]
fins = 0.75
Uins_tot = fins*Uins

print "The total heat transfer coefficient on insulation is " + str(Uins) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on insulation with 0.75 fraction area is " + str(Uins_tot) + " (W/m^2 deg C)"
print "*********************"

Utot = Ustud_tot + Uins_tot
print "Thus, the overall heat transfer coefficient of the wall is " + str(Utot) + " (W/m^2 deg C)"
print "***************************"

# Area of the wall
Atot = 50*2.5
Awall = 0.8*Atot
print "The total area of the wall is " + str(Awall) + " (m^2)"
print "******************"

# Q total
Tin = 22
Tout = -2
DT=Tin-Tout
Q = Utot*Awall*DT
Qtot = Q/1000
print "Thus, the total heat transfer rate of the wall is " + str(Qtot) + " (kW)"