#Conductive Resistances in Series
RF = {"Name": "Foam", "A": 0.25, "L": 0.03, "k": 0.026} #Foam layer
RPS = {"Name": "Plaster Layer", "A": 0.25, "L": 0.02, "k": 0.22} #Plaster layer

#Conductive Resistances in Parallel
RB = {"Name": "Brick", "A": 0.22, "L": 0.16, "k": 0.72} #Brick
RPP = {"Name": "Palster Layer", "A": 0.015, "L": 0.16, "k": 0.22} #Plaster layer

#Convective Resistances
Rin = {"Name": "Internal", "A": 0.25, "h": 10} #internal
Rout = {"Name": "External", "A": 0.25, "h": 25} #external

ListOfRcond = [RF, RPS, RPS]
ListOfRpar = [RB, RPP, RPP]
ListOfRconv = [Rin, Rout]

totalRcondValue = 0

for anyResistance in ListOfRcond:
    L_anyResistance = anyResistance["L"] 
    A_anyResistance = anyResistance["A"]
    k_anyResistance = anyResistance["k"]
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)
    totalRcondValue = totalRcondValue + RValue_anyResistance

print "the total conductive resistance is " + str(totalRcondValue) +str(" deg C/W")
    
totalRparValue = 0

for anyResistance in ListOfRpar:
    L_anyResistance = anyResistance["L"] 
    A_anyResistance = anyResistance["A"]
    k_anyResistance = anyResistance["k"]
    RValue_anyResistance = (A_anyResistance*k_anyResistance)/L_anyResistance
    totalRparValue = totalRparValue + RValue_anyResistance
   
totalRparValue = (totalRparValue)**(-1)

print "the total parallel resistance is " + str(totalRparValue) +str(" deg C/W")

totalRconvValue = 0

for anyResistance in ListOfRconv: 
    A_anyResistance = anyResistance["A"]
    h_anyResistance = anyResistance["h"]
    RValue_anyResistance = 1/(A_anyResistance*h_anyResistance)
    totalRconvValue = totalRconvValue + RValue_anyResistance
    
print "the total convective resistance is " + str(totalRconvValue) +str(" deg C/W")
    
Rtot = totalRcondValue + totalRparValue + totalRconvValue

print "total resistance is: " + str(Rtot) +str(" deg C/W")