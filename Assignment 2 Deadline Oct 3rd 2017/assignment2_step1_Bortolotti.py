#Conductive Resistances in Series
RF = [0.25,0.03,0.026] #Foam layer - the values correspond to A, L, k: Area [0 = position], Length [1], K [2]
RPS = [0.25,0.02,0.22] #Plaster layer

#Conductive Resistances in Parallel
RB = [0.22,0.16,0.72] #Brick
RPP = [0.015, 0.16,0.22] #Plaster layer

#Convective Resistances
Rin = [0.25,10] #internal - A [0], Convective heat transfer coefficient [1]
Rout = [0.25,25] #external

ListOfRcond = [RF, RPS, RPS] #lists inside the ListOfResistances
ListOfRpar = [RB, RPP, RPP]
ListOfRconv = [Rin, Rout]

totalRcondValue = 0

for anyResistance in ListOfRcond:
    L_anyResistance = anyResistance[1] 
    A_anyResistance = anyResistance[0]
    k_anyResistance = anyResistance[2]
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)
    totalRcondValue = totalRcondValue + RValue_anyResistance

print "the total conductive resistance is " + str(totalRcondValue) +str(" deg C/W")
    
totalRparValue = 0

for anyResistance in ListOfRpar:
    L_anyResistance = anyResistance[1] 
    A_anyResistance = anyResistance[0]
    k_anyResistance = anyResistance[2]
    RValue_anyResistance = (A_anyResistance*k_anyResistance)/L_anyResistance
    totalRparValue = totalRparValue + RValue_anyResistance
   
totalRparValue = (totalRparValue)**(-1)

print "the total parallel resistance is " + str(totalRparValue) +str(" deg C/W")

totalRconvValue = 0

for anyResistance in ListOfRconv: 
    A_anyResistance = anyResistance[0]
    h_anyResistance = anyResistance[1]
    RValue_anyResistance = 1/(A_anyResistance*h_anyResistance)
    totalRconvValue = totalRconvValue + RValue_anyResistance
    
print "the total convective resistance is " + str(totalRconvValue) +str(" deg C/W")
    
Rtot = totalRcondValue + totalRparValue + totalRconvValue

print "total resistance is: " + str(Rtot) +str(" deg C/W")
