
#-------------------- ASSIGNMENT 2 STEP 1 -------------------------------
# -------------------------Using List------------------------------------

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

Rf = [0.25,0.03,0.026] # Area = 0.25, L = 0.03, kf = 0.026
Rp1 = [0.25,0.02,0.22] # Area = 0.25, L = 0.02, kp = 0.022
Rp2 = [0.25,0.02,0.22] # Area = 0.25, L = 0.02, kp = 0.022

ListOfRcondS = [Rf,Rp1,Rp2]

Total_Rvalue1 = 0

for RcondS in ListOfRcondS:
    L_RcondS = RcondS[1]
    A_RcondS = RcondS[0]
    k_RcondS = RcondS[2]
    
    Rvalue_RcondS = L_RcondS/(A_RcondS*k_RcondS)
    
    Total_Rvalue1=Total_Rvalue1+Rvalue_RcondS
    
print "The Total Resistance of Conductive Series is " + str(Total_Rvalue1) + " (degC/W)"
print "------------------------------------------------------------------"

    
# Convective Resistance in Series

Rconv1 = [0.25,10] # Area = 0.25, h1 = 10
Rconv2 = [0.25,25] # Area = 0.25, h2 = 25

ListOfRconvS = [Rconv1,Rconv2]

Total_Rvalue2 = 0

for RconvS in ListOfRconvS:
    A_RconvS = RconvS[0]
    h_RconvS = RconvS[1]
    
    Rvalue_RconvS = 1/(A_RconvS*h_RconvS)
    
    Total_Rvalue2=Total_Rvalue2+Rvalue_RconvS
   
print "The Total Resistance of Convective Series is " + str(Total_Rvalue2) + " (degC/W)"
print "------------------------------------------------------------------"


# Conductive Resistance in Parallel

Rpp1 = [0.015,0.16,0.22] # Area = 0.015, L = 0.16, kp = 0.22
Rb = [0.22,0.16,0.72] # Area = 0.22, L = 0.16, kb = 0.72
Rpp2 = [0.015,0.16,0.22] # Area = 0.15, L = 0.16, kp = 0.22

ListOfRcondP = [Rpp1,Rb,Rpp2]

Total_Rvalue3 = 0

for RcondP in ListOfRcondP:
    L_RcondP = RcondP[1]
    A_RcondP = RcondP[0]
    k_RcondP = RcondP[2]
    
    Rvalue_RcondP = L_RcondP / (A_RcondP*k_RcondP) # Calculate each Resistance
    
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

