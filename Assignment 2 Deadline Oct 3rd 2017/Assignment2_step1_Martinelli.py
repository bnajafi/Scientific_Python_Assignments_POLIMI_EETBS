#horizontal and vertical are inteded as seen in figure
H = 3.0
L = 5.0 #wall dimensions

Tin = 20.0
Tout = -10.0 #temperatures

Rf = [0.25,0.03,0.026] #foam: area = 0 lenght = 1 conductivity = 2
Rsp = [0.25,0.02,0.22] #series plaster: area = 0 lenghtv = 1 conductivity = 2
Rpp = [0.015,0.16,0.22] #parallel plaster: area = 0 lenght = 1 conductivity = 2
Rb = [0.22,0.16,0.72] #brick: area = 0 lenght = 1 conductivity = 2
Rin = [0.25,10.0] #internal convective resistance: area = 0 coefficient = 1
Rout = [0.25,25.0] #external convective resistance: area = 0 coefficient = 1

LcondS = [Rf,Rsp,Rsp] #list of series conductive resistances
LcondP = [Rb,Rpp,Rpp] #list of parallel conductive resistances
Lconv = [Rin,Rout] #list of convective resistances

RtotS = 0 #series resistance value
for anyResistance in LcondS: 
    L_R = anyResistance[1]
    A_R = anyResistance[0]
    k_R = anyResistance[2]
    RValue_R = L_R/(A_R*k_R)
    RtotS = RtotS + RValue_R
print "the total conductive series resistance is: " + str(RtotS) + " (degC/W)"

RtotP = 0 #parallel resistance value
for anyResistance in LcondP:
    L_R = anyResistance[1]
    A_R = anyResistance[0]
    k_R = anyResistance[2]
    RValue_R = L_R/(A_R*k_R)
    RtotP = RtotP + 1/RValue_R
RtotP = RtotP**(-1)
print "the total conductive parallel resistance is: " + str(RtotP) + " (degC/W)"

RtotC = 0 #convective resistance value
for anyResistance in Lconv:
    A_R = anyResistance[0]
    h_R = anyResistance[1]
    RValue_R = 1/(A_R*h_R)
    RtotC = RtotC + RValue_R
print "the total convective resistance is: " + str(RtotC) + " (degC/W)"

Rtot= RtotS + RtotP + RtotC
print "the total resistance is: " + str(Rtot) + " (degC/W)"

Q = (Tin - Tout)/Rtot
print "the rate of heat transfer through the wall for each unit is "+str(Q)+ " (W)"
Qtot = (Q*H*L)/0.25
print "the total rate of heat transfer through the wall is "+str(Qtot)+ " (W)"