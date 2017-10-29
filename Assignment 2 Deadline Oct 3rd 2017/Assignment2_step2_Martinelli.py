#horizontal and vertical are inteded as seen in figure
H = 3.0
L = 5.0 #wall dimensions

Tin = 20.0
Tout = -10.0 #temperatures

Rf = {"name":"foam","area":0.25,"lenght":0.03,"k":0.026,"ResValue":0}
Rsp = {"name":"series plaster","area":0.25,"lenght":0.02,"k":0.22,"ResValue":0}
Rpp = {"name":"parallel plaster","area":0.015,"lenght":0.16,"k":0.22,"ResValue":0}
Rb = {"name":"brick","area":0.22,"lenght":0.16,"k":0.72,"ResValue":0}
Rin = {"name":"internal convection","area":0.25,"h":10.0,"ResValue":0}
Rout = {"name":"external convection","area":0.25,"h":25.0,"ResValue":0}

LcondS = [Rf,Rsp,Rsp] #list of series conductive resistances
LcondP = [Rb,Rpp,Rpp] #list of parallel conductive resistances
Lconv = [Rin,Rout] #list of convective resistances

RtotS = 0 #series resistance value
for anyResistance in LcondS:
    L_R = anyResistance["lenght"]
    A_R = anyResistance["area"]
    k_R = anyResistance["k"]
    RValue_R = L_R/(A_R*k_R)
    anyResistance["ResValue"] = RValue_R
    RtotS = RtotS + RValue_R
print "the total conductive series resistance is: " + str(RtotS) + " (degC/W)"

RtotP = 0 #parallel resistance value
for anyResistance in LcondP:
    L_R = anyResistance["lenght"]
    A_R = anyResistance["area"]
    k_R = anyResistance["k"]
    RValue_R = L_R/(A_R*k_R)
    anyResistance["ResValue"] = RValue_R
    RtotP = RtotP + 1/RValue_R
RtotP = RtotP**(-1)
print "the total conductive parallel resistance is: " + str(RtotP) + " (degC/W)"

RtotC = 0 #convective resistance value
for anyResistance in Lconv:
    A_R = anyResistance["area"]
    h_R = anyResistance["h"]
    RValue_R = 1/(A_R*h_R)
    anyResistance["ResValue"] = RValue_R
    RtotC = RtotC + RValue_R
print "the total convective resistance is: " + str(RtotC) + " (degC/W)"

Rtot= RtotS + RtotP + RtotC
print "the total resistance is: " + str(Rtot) + " (degC/W)"

Q = (Tin - Tout)/Rtot
print "the rate of heat transfer through the wall for each unit is "+str(Q)+ " (W)"
Qtot = (Q*H*L)/0.25
print "the total rate of heat transfer through the wall is "+str(Qtot)+ " (W)"