# Assignment 2

# Temperatures (C)
Tin=20
Tout=-10

# Geometric parameters of the wall (m)
W=5
H=3

#Resistances

RConv_in={'Res_value':0,'name':'inner foam surface resistance', 'area':0.25, 'h':10}
RConv_ex={'Res_value':0,'name':'outer plaster surface resistance', 'area':0.25, 'h':25}
R1={'Res_value':0,'name':'foam layer resistance', 'area':0.25, 'length':0.03,'conductivity':0.026}
R2={'Res_value':0,'name':'plaster layer horizontal resistance 1', 'area':0.25, 'length':0.02,'conductivity':0.22}
R3={'Res_value':0,'name':'plaster layer vertical resistance', 'area':0.015, 'length':0.16,'conductivity':0.22}
R4={'Res_value':0,'name':'brick resistance', 'area':0.22, 'length':0.16,'conductivity':0.72}
R5={'Res_value':0,'name':'plaster layer vertical resistance 2', 'area':0.015, 'length':0.16,'conductivity':0.22}
R6={'Res_value':0, 'name':'plaster layer horizontal resistance 2', 'area':0.25, 'length':0.02,'conductivity':0.22}


#Convective resistances
ListOfConv_Resistance=[RConv_in,RConv_ex]
#Calculating resistances
for anyResistance in ListOfConv_Resistance:
     RValue_anyResistance=1/(anyResistance['area']*anyResistance['h'])
     anyResistance['Res_value']=RValue_anyResistance
#Print resistances
for anyResistance in ListOfConv_Resistance:
    print('The value of the '+str(anyResistance['name'])+' is: '+ str(anyResistance['Res_value'])+' C/W')


#Conductive Series resistances
ListOfCond_ResistanceInSeries=[ R1, R2, R6]
#Calculating resistances
for anyResistance in ListOfCond_ResistanceInSeries:
     RValue_anyResistance=anyResistance['length']/(anyResistance['area']*anyResistance['conductivity'])
     anyResistance['Res_value']=RValue_anyResistance
#Printing Resistances
for anyResistance in ListOfCond_ResistanceInSeries:
    print('The value of the '+str(anyResistance['name'])+' is: '+ str(anyResistance['Res_value'])+' C/W')


#Conductive Parallel resistances
ListOfCond_ResistanceInParallel=[ R3, R4, R5]
#Calculating resistances
for anyResistance in ListOfCond_ResistanceInParallel:
     RValue_anyResistance=anyResistance['length']/(anyResistance['area']*anyResistance['conductivity'])
     anyResistance['Res_value']=RValue_anyResistance
#Printing Resistances
for anyResistance in ListOfCond_ResistanceInParallel:
    print('The value of the '+str(anyResistance['name'])+' is: '+ str(anyResistance['Res_value'])+' C/W')

#Parallel 
R_parallel=(1/R3['Res_value']+1/R4['Res_value']+1/R5['Res_value'])**-1

#Total resistance
Rtot=R1['Res_value']+R2['Res_value']+R6['Res_value']+RConv_in['Res_value']+RConv_ex['Res_value']+R_parallel
#Or in different way
#Rtot=0
#ListOfR=[RConv_in['Res_value'], RConv_ex['Res_value'], R1['Res_value'], R2['Res_value'],R_parallel, R6['Res_value']]
#for anyR in ListOfR:
#    Rtot=Rtot+anyR
    
#print Rtot

#Rate of Heat Transfer 
Q_dot=(H/0.25)*W*((Tin-Tout)/Rtot)

#Printing results
print(' ')
print('The total thermal resistence of the wall section is: '+str(Rtot)+' C/W');
print('The rate of heat transfer through the wall is: '+str(Q_dot)+' W')

