# Assignment 2

# Temperatures (C)
Tin=20
Tout=-10

# Geometric parameters of the wall (m)
W=5
H=3

#Initializating resistances

RConv_in=[0.25, 10] # internal surface, area in m2:0 , h in W/m2:1
RConv_ex=[0.25, 25] # external surface, area in m2:0 , h in W/m2:1
R1=[0.25, 0.03, 0.026] # foam layer, area in m2:0, length in m:1, conductivity in W/m:2
R2=[0.25, 0.02, 0.22] # plaster layer vertical, area in m2:0, length in m:1, conductivity in W/m:2
R3=[0.015, 0.16, 0.22] # plaster horizontal layer, area in m2:0, length in m:1, conductivity in W/m:2
R4=[0.22, 0.16, 0.72] # brick, area in m2:0, length in m:1, conductivity in W/m:2
R5=[0.015, 0.16, 0.22] # plaster horizontal layer, area in m2:0, length in m:1, conductivity in W/m:2
R6=[0.25, 0.02, 0.22] # plaster layer vertical, area in m2:0, length in m:1, conductivity in W/m:2


#Convective resistances
ListOfConv_Resistance=[RConv_in,RConv_ex]
RConv=[]
for anyResistance in ListOfConv_Resistance:
     RValue_anyResistance=1/(anyResistance[0]*anyResistance[1])
     RConv.append(RValue_anyResistance)

#Conductive resistances in series 
ListOfCond_ResistanceInSeries=[ R1, R2, R6]
RCond_Series=[]
for anyResistance in ListOfCond_ResistanceInSeries:
     RValue_anyResistance=anyResistance[1]/(anyResistance[0]*anyResistance[2])
     RCond_Series.append(RValue_anyResistance)
     
#Conductive resistances in parallel 
ListOfCond_ResistanceInParallel=[ R3, R4, R5]
RCond_Parallel=[]
for anyResistance in ListOfCond_ResistanceInParallel:
     RValue_anyResistance=anyResistance[1]/(anyResistance[0]*anyResistance[2])
     RCond_Parallel.append(RValue_anyResistance)

#Parallel 
R_parallel=(1/RCond_Parallel[0]+1/RCond_Parallel[1]+1/RCond_Parallel[2])**-1

#Total resistance
Rtot=RCond_Series[0]+RCond_Series[1]+R_parallel+RCond_Series[2]+RConv[0]+RConv[1]

#Rate of Heat Transfer 
Q_dot=(H/0.25)*W*((Tin-Tout)/Rtot)

#Printing results
print('The total thermal resistence of the wall section is: '+str(Rtot)+' C/W');
print('The rate of heat transfer through the wall is: '+str(Q_dot)+' W')
