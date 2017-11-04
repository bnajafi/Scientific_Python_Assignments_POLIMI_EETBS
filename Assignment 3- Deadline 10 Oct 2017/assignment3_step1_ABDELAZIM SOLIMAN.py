Material_Library = { "Sout_Winter":0.03,"Sin": 0.12,"Glass Insul.":2.52, "WoodStud":0.63, "Woodfiber": 0.23, "WoodBevel": 0.14, "Gyp.wall":0.079}  
        
CLY = ["Sout_Winter","Sin"]  #CONVECTIVE LAYER


# THE RESISTANCES 
# FOR WOOD STUD
SLY = ["WoodBevel","Woodfiber", "WoodStud","Gyp.wall"]   #STUD LAYER

Tot_SLY = SLY + CLY
RTot_SLY = 0 
RValues_SLY = []
for Rstud in Tot_SLY:
    RValueStud = Material_Library[Rstud]
    Rtot_Stud = RTot_SLY + RValueStud
    RValues_SLY.append(RValueStud)
print "The value of each resist in Stud  = " + str(RValues_SLY)
print "Rtot_Stud = "+str(Rtot_Stud) +" degC/W" 

# FOR GLASS INSUL.
GLY = ["WoodBevel","Woodfiber","Glass Insul.","Gyp.wall"]   #Glass Insulation LAYER

Tot_GLY = GLY + CLY
RTotGLY = 0 
RValues_GLY = []
for Rglass in Tot_GLY:
    Rvalue_glass = Material_Library[Rglass]
    Rtot_glass = RTotGLY + Rvalue_glass
    RValues_GLY.append(Rvalue_glass)
print "The value of each resist. in  glass insul. layer = " + str(RValues_GLY)
print "Rtot_glass = " + str(Rtot_glass) + " (m^2 DegC/W)"    
    
# THE OVERALL HEAT COEFFICINT {U} 

# FOR STUD
Ust = 1/Rtot_Stud
fst = 0.25 
Ust_tot = fst*Ust
 # FOR GLASS INSUL.
Uglass = 1/Rtot_glass
fglass = 0.75
Uglass_tot = fglass*Uglass
#TOTAL U
U_tot = Uglass_tot + Ust_tot
print "TOTAL U  = " + str(U_tot) + " (W/m^2 deg C)"

#the total rate of H. TRANS.
Tin = 22
Tout = -2
DT=Tin-Tout
Awall = 0.8*50*2.5
Q = (U_tot*Awall*DT)/1000
print "Q = " + str(Q) + " (KW)"







