#Calculating total resistance using the "list function []"
#Conduction resistance in series
R1 = [0.25,0.03,0.026] # Foam layer;  Area,Lenght,k
R2 = [0.25,0.02,0.22] # Plaster 1 layer; Area,Lenght,k
R3 = [0.25,0.02,0.22] # Plaster 2 later; Area,Lenght,k
#Conduction resistance in parallel
R4 = [0.015,0.16,0.22] # Plaster 3 layer; Area,Lenght,k
R5 = [0.22,0.16,0.72] # Brick layer; Area,Lenght,k
R6 = [0.015,0.16,0.22] # Plaster 4 layer; Area,Lenght,k
#Convection resistance in series
R7 = [0.25,10] # Convection resistance entering; Area,h
R8 = [0.25,25] # Convection resistance leaving; Area,h
#Lists of Resistances in list
Cond_Res_Series = [R1,R2,R3] # List of conduction resistances in series
Cond_Res_Parallel = [R4,R5,R6] # List of conduction resistances in parallel
Conv_Res = [R7,R8] #List of convection resistances

#Calculating conductve resistance in series
print 'To calculate the conductive resistance in series;'
Tot_rescondseries=0
for anyreslist in Cond_Res_Series:
    print 'The list of parameters in this material is:'
    print anyreslist
    A_anyreslist=anyreslist[0]
    L_anyreslist=anyreslist[1]
    k_anyreslist=anyreslist[2]
    Res_condseries=L_anyreslist/(k_anyreslist*A_anyreslist)
    Tot_rescondseries=Tot_rescondseries+Res_condseries
    print 'The calculated conductive resistance in this material is ' + str(Res_condseries) +' degC/W'
    print '---------------------------'
print 'And the total conductive resistance in series is ' +str(Tot_rescondseries) +'  degC/W'
print '*******************************************************'

#Calculating conductve resistance in parallel
print 'To calculate the conductive resistance in parallel;'
Tot_rescondparallel=0
Sum_condparallel=0
for anyreslist in Cond_Res_Parallel:
    print 'The list of parameters in this material is:'
    print anyreslist
    A_anyreslist=anyreslist[0]
    L_anyreslist=anyreslist[1]
    k_anyreslist=anyreslist[2]
    Res_condparallel=L_anyreslist/(k_anyreslist*A_anyreslist)
    Sum_condparallel=Sum_condparallel+(1/Res_condparallel)
    print 'The calculated conductive resistance in this material is ' + str(Res_condparallel) +' degC/W'
    print '---------------------------'
Tot_rescondparallel=Tot_rescondparallel+(1/Sum_condparallel)
print 'And the total conductive resistance in series is ' +str(Tot_rescondparallel) +'  degC/W'
print '**********************************************'

#Calculating convection resistance in in series
print 'To calculate the convection resistance entering and leaving the unit;'
Tot_resconv=0
for anyreslist in Conv_Res:
    print 'The list of parameters in this material is:'
    print anyreslist
    A_anyreslist=anyreslist[0]
    h_anyreslist=anyreslist[1]
    Res_conv=1/(A_anyreslist*h_anyreslist)
    Tot_resconv=Tot_resconv+(Res_conv)
    print 'The calculated convection resistance in this material is ' + str(Res_conv) +' degC/W'
    print '---------------------------'
print 'And the total convection resistance in series is ' +str(Tot_resconv) +'  degC/W'
print '**********************************************'
print '**********************************************'

totres_unit=Tot_resconv+Tot_rescondparallel+Tot_rescondseries
print 'Hence the sum of total resistance across the unit is ' +str(totres_unit) +'  degC/W'

T1=20 # in (degC)
T2=-10 # in (degC)
A_unit=0.25# in (m2)
A_block=15 # in (m2)
H_unit=(T1-T2)/totres_unit # in (W)
H_block=H_unit*A_block/A_unit # in (W)
print'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*'
print 'The calculated heat flux across the unit is ' +str(H_unit) +' W ' 'hence the total heat flux across the whole block is ' +str(H_block) +' W'
print '****************************************THANK YOU FOR YOUR ATTENTION************************************************'