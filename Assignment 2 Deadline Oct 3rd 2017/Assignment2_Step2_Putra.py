
#-------------------- ASSIGNMENT 2 STEP 2 -------------------------------
# ---------------------Using Dictionary----------------------------------

# Name : Hendra Suryana Putra

# Heat loss through a composite wall

# Thermal Conductivity and Convection Heat Transfer on Example D


# Definition
# kf = Thermal Conductivity of Foam
# kp = Thermal Conductivity of Plaster
# kb = Thermal Conductivity of Brick
# h1 = Convection heat transfer of Inner Side
# h2 = Convection heat transfer of Outer side 
# RcondS = Total Resistance of Conductive Series
# RconvS = Total Resistance of Convective Series
# RcondP = Total Resistance of Conductive Parallel


# Conductive Resistance in Series

Rf = {"name":"foam","area":0.25,"length":0.03,"k":0.026,"ResValue":0}
Rp1 = {"name":"Plaster 1","area":0.25,"length":0.02,"k":0.22,"ResValue":0}
Rp2 = {"name":"Plaster 2","area":0.25,"length":0.02,"k":0.22,"ResValue":0}

ListOfRcondS = [Rf,Rp1,Rp2]

Total_Rvalue1 = 0

for RcondS in ListOfRcondS:
    L_RcondS = RcondS["length"]
    A_RcondS = RcondS["area"]
    k_RcondS = RcondS["k"]
    
    name_RcondS = RcondS["name"]

    Rvalue_RcondS = L_RcondS/(A_RcondS*k_RcondS)
     
    RcondS["ResValue"]=Rvalue_RcondS 
    
    print "The calculated Resistance of " + name_RcondS + " is " + str(Rvalue_RcondS)+ " (degC/W)"

    Total_Rvalue1=Total_Rvalue1+Rvalue_RcondS
    
print "The Total Resistance of Conductive Series is " + str(Total_Rvalue1) + " (degC/W)"
print "------------------------------------------------------------------"
    
# Convective Resistance in Series

Rconv1 = {"name":"Inner Side","area":0.25,"h":10,"ResValue1":0}
Rconv2 = {"name":"Outer Side","area":0.25,"h":25,"ResValue1":0}


ListOfRconvS = [Rconv1,Rconv2]

Total_Rvalue2 = 0

for RconvS in ListOfRconvS:
    A_RconvS = RconvS["area"]
    h_RconvS = RconvS["h"]
    name_RconvS = RconvS["name"]
    
    Rvalue_RconvS = 1/(A_RconvS*h_RconvS)
    
    RconvS["ResValue1"]=Rvalue_RconvS
    
    print "The calculated Resistance of " + name_RconvS + " is " + str(Rvalue_RconvS) + " (degC/W)"

    Total_Rvalue2=Total_Rvalue2+Rvalue_RconvS
   
print "The Total Resistance of Convective Series is " + str(Total_Rvalue2) + " (degC/W)"
print "------------------------------------------------------------------"

# Conductive Resistance in Parallel

Rpp1 = {"name":"Parallel Plaster 1","area":0.015,"length":0.16,"k":0.22,"ResValue2":0}
Rb = {"name":"Brick","area":0.22,"length":0.16,"k":0.72,"ResValue2":0}
Rpp2 = {"name":"Parallel Plaster 2","area":0.015,"length":0.16,"k":0.22,"ResValue2":0}


ListOfRcondP = [Rpp1,Rb,Rpp2]

Total_Rvalue3 = 0

for RcondP in ListOfRcondP:
    L_RcondP = RcondP["length"]
    A_RcondP = RcondP["area"]
    k_RcondP = RcondP["k"]
    
    name_RcondP = RcondP["name"]
    
    Rvalue_RcondP = L_RcondP/(A_RcondP*k_RcondP) # Calculate each Resistance
    
    print "The calculated Resistance of " + name_RcondP + " is " + str(Rvalue_RcondP) + " (degC/W)"

    Rvalue_RcondPA = 1/Rvalue_RcondP # Calculate each 1/Resistance

    Total_Rvalue3=Total_Rvalue3+Rvalue_RcondPA # Calculate the sum of each 1/R
    
Total_Rvalue3P=1/Total_Rvalue3 # Calculate the Total Parallel Resistance

print "The Total Resistance of Conductive Parallel is " + str(Total_Rvalue3P) + " (degC/W)"
print "------------------------------------------------------------------"

# Overall Resistance of the wall

Rtotal = Total_Rvalue1+Total_Rvalue2+Total_Rvalue3P

print "Thus, The overall resistance of the wall is " + str(Rtotal) + " (degC/W)"
 


#---------------------------------------------------------------------------

# Temperature

Tin = 20
Tout = -10

DT=Tin-Tout

#---------------------------------------------------------------------------

# Heat transfer Rate

Qtot=DT/Rtotal
print "------------------------------------------------------------------"
print "------------------------------------------------------------------"
print "Thus, The Heat Transfer Rate through the system is " +str(Qtot)+ "(W)"

