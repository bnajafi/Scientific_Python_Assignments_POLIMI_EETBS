#Rachid Aamrani

#Conduction resistance in series

R1 = {'area':0.25,'length':0.03,"k":0.026} # Foam layer
R2 = {'area':0.25,'length':0.02,"k":0.22} # Plaster 1 layer
R3 = {'area':0.25,'length':0.02,"k":0.22} # Plaster 2 layer

#Conduction resistance in parallel

R4 = {'area':0.015,'length':0.16,"k":0.22} # Plaster 3 
R5 = {'area':0.22,'length':0.16,"k":0.72} # Brick layer
R6 = {'area':0.015,'length':0.16,"k":0.22} # Plaster 4 layer

#Convection resistance in series

R7 = {'area':0.25,'h':10} # Convection resistance entering
R8 = {'area':0.25,'h':25} # Convection resistance leaving

#definitions of Resistances in list

Cond_Res_Series = [R1,R2,R3] # List of conduction resistances in series
Cond_Res_Parallel = [R4,R5,R6] # List of conduction resistances in parallel
Conv_Res = [R7,R8] #List of convection resistances
 
#Calculating conductve resistance in series
print 'To calculate the conductive resistance in series;'
Tot_rescondseries=0
for anyreslist in Cond_Res_Series:
    print 'The charactericts of material are:'
    print anyreslist
    A_anyreslist=anyreslist['area']
    L_anyreslist=anyreslist['length']
    k_anyreslist=anyreslist['k']
    Res_condseries=L_anyreslist/(k_anyreslist*A_anyreslist)
    Tot_rescondseries=Tot_rescondseries+Res_condseries
    print 'Conductive resistance in this material is ' + str(Res_condseries) +' degC/W'
    print '---------------------------'
print 'And the total conductive resistance in series is ' +str(Tot_rescondseries) +'  degC/W'
print '*******************************************************'
 
#Calculating conductve resistance in parallel
print 'Conductive resistance in parallel;'
Tot_rescondparallel=0
Sum_condparallel=0
for anyreslist in Cond_Res_Parallel:
    print 'The charactericts of material are:'
    print anyreslist
    A_anyreslist=anyreslist['area']
    L_anyreslist=anyreslist['length']
    k_anyreslist=anyreslist['k']
    Res_condparallel=L_anyreslist/(k_anyreslist*A_anyreslist)
    Sum_condparallel=Sum_condparallel+(1/Res_condparallel)
    print 'Conductive resistance in this material is ' + str(Res_condparallel) +' degC/W'
    print '---------------------------'
Tot_rescondparallel=Tot_rescondparallel+(1/Sum_condparallel)
print 'And the total conductive resistance in series is ' +str(Tot_rescondparallel) +'  degC/W'
print '**********************************************'
 
#Calculating convection resistance in in series
print 'In order to compute the convection resistance entering the unit;'
Tot_resconv=0
for anyreslist in Conv_Res:
    print 'The charactericts of material are::'
    print anyreslist
    A_anyreslist=anyreslist['area']
    h_anyreslist=anyreslist['h']
    Res_conv=1/(A_anyreslist*h_anyreslist)
    Tot_resconv=Tot_resconv+(Res_conv)
    print 'Convection resistance in this material is ' + str(Res_conv) +' degC/W'
    print '---------------------------'
print 'And the total convection resistance in series is ' +str(Tot_resconv) +'  degC/W'
print '**********************************************'
print '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'
 
totres_unit=Tot_resconv+Tot_rescondparallel+Tot_rescondseries
print 'Hence the total resistance across the unit is ' +str(totres_unit) +'  degC/W'
print'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*'
T1=20 # in (degC)
T2=-10 # in (degC)
A_unit=0.25# in (m2)
A_block=15 # in (m2)
H_unit=(T1-T2)/totres_unit # in (W)
H_block=H_unit*A_block/A_unit # in (W)
print 'The  heat flow across the unit is ' +str(H_unit) +' W ' 'hence the total heat fluow is ' +str(H_block) +' W'
