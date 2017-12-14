
#-------------------- ASSIGNMENT 5 STEP 1 -------------------------------
# -------------------------Using Numpy------------------------------------

# Name : Hendra Suryana Putra

# Heat loss through a composite wall

# Thermal Conductivity and Convection Heat Transfer on Example D


import numpy as np

# Resistance in Series

R_names = np.array(["Rconv1","Rp1","Rf","Rp2","Rconv2"])
R_types = np.array(["conv","cond","cond","cond","conv"])
R_h = np.array([10,None,None,None,25])
R_k = np.array([None,0.22,0.026,0.22,None])
R_L = np.array([None,0.02,0.03,0.02,None])
R_RValues= np.array(np.zeros(5))

R_RValues[R_types=="cond"] = R_L[R_types=="cond"]/ R_k[R_types=="cond"]
R_RValues[R_types=="conv"] = 1.0 / R_h[R_types=="conv"]
R_Rtot_Ser=R_RValues.sum()

R_A = 0.25
Rtot_ser = R_Rtot_Ser/R_A

print "The Total Resistance in Series is " + str(Rtot_ser) + " (degC/W)"
print "------------------------------------------------------------------"

# Resistance in Parallel

R_names1 = np.array(["Rpp1","Rb","Rpp2"])
R_kp = np.array([0.22,0.72,0.22])
R_Ap = np.array([0.015,0.22,0.015])
R_RValues1= np.array(np.zeros(5))
R_RValues1=R_Ap*R_kp
R_Lp = 0.16
R_RValues1=R_Lp/R_RValues1
R_RValues1=1/R_RValues1

R_Rtot_Par = R_RValues1.sum()

Rtot_Par = 1/R_Rtot_Par

print "The Total Resistance in Parallel is " + str(Rtot_Par) + " (degC/W)"
print "------------------------------------------------------------------"

# Resistance of the wall

Rtotal = Rtot_ser+Rtot_Par

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

