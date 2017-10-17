def wall_calc(defineYourLayer):
 
    Material_Library = { "Sout_Winter":0.03,"Sin": 0.12,"Glass Insul.":2.52, "WoodStud":0.63, "Woodfiber": 0.23, "WoodBevel": 0.14, "Gyp.wall":0.079}  
    conv_layer = ["Sout_Winter","Sin"]
     
    # Calculate the total Resistance Value 
     
    yourNewLayer = defineYourLayer + conv_layer
     
    print "The layer consist of " + str(defineYourLayer)
     
    Rtotal = 0
    Rvalue_NewLayer = []
     
    for RNewLayer in yourNewLayer:
        Rvalue_new = Material_Library[RNewLayer]
        Rtotal = Rtotal + Rvalue_new
        Rvalue_NewLayer.append(Rvalue_new)
         
    print "Total Resistance = " + str(Rtotal) + " (m^2 DegC/W)"
    result = {"R total":Rtotal,"All R value of New Layer":Rvalue_NewLayer}
      
    return result
 
# FOR WOOD STUD
SLY = ["WoodBevel","Woodfiber", "WoodStud","Gyp.wall"]
     
Rtot_stud = wall_calc(SLY)
Ustud = 1/Rtot_stud["R total"]
fstud = 0.25
Ustud_tot = fstud*Ustud
print " Ustud_tot =  " + str(Ustud_tot) + " (W/m^2 deg C)"

# FOR GLASS INSUL.
GLY = ["WoodBevel","Woodfiber","Glass Insul.","Gyp.wall"]   #Glass Insulation LAYER
Rtot_GLASS = wall_calc(GLY)
UGLASS = 1/Rtot_GLASS["R total"]
fGLASS = 0.75
UGLASS_tot = fGLASS*UGLASS

print "UGLASS_tot " + str(UGLASS_tot) + " (W/m^2 deg C)"

 
 
# Calculate the U Total of the wall ----------------------------------------------------
 
U_tot = Ustud_tot + UGLASS_tot
 
print "TOTAL U = " + str(U_tot) + " (W/m^2 deg C)"

 
 
#the total rate of H. TRANS.
Tin = 22
Tout = -2
DT=Tin-Tout
Awall = 0.8*50*2.5
Q = (U_tot*Awall*DT)/1000
print "Q = " + str(Q) + " (KW)"