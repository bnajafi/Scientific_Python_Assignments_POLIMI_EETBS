#Assignment 2
#Name:Shashwat Parsana
#STEP:2

Ri={'name':'Inner Wall','h':10,'Area':0.25,'Res_Value':0}
R1={'name':'Foam','Lenght':0.03,'Conductivity':0.026,'Area':0.25,'Res_Value':0} 
R2={'name':'Plaster towards inner surface','Lenght':0.02,'Conductivity':0.22,'Area':0.25,'Res_Value':0}
R3={'name':'Plaster above brick','Lenght':0.16,'Conductivity':0.22,'Area':0.015,'Res_Value':0}
R4={'name':'Brick','Lenght':0.16,'Conductivity':0.72,'Area':0.22,'Res_Value':0}
R5={'name':'Plaster below brick','Lenght':0.16,'Conductivity':0.22,'Area':0.015,'Res_Value':0}
R6={'name':'Plaster towards outer surface','Lenght':0.02,'Conductivity':0.22,'Area':0.25,'Res_Value':0}
Ro={'name':'Outer wall','h':25,'Area':0.25,'Res_Value':0}


#Conductive Resistance in Parallel
ListofResistance_parallel=[R3,R4,R5]
total_parallel_res=0
print'*********************************************************************************************************'
print'Below are the individual calculated resistance in parallel i.e. Plaster above brick,Brick and Plaster below brick, respectively:'
print'******'
for anyresistance in ListofResistance_parallel:
    L_anyresistance=anyresistance['Lenght']
    k_anyresistance=anyresistance['Conductivity']
    A_anyresistance=anyresistance['Area']
    Res_value=L_anyresistance/(k_anyresistance*A_anyresistance)
    total_parallel_res=total_parallel_res+(1/Res_value)
    total_parallel2_res=1/total_parallel_res
    name_resistanceP=anyresistance['name']
    print'The calculated Resistance of '+name_resistanceP+' is '+str(Res_value) +' (degC/W)'
    print'******'
print'So,The total sum of resistance in Parallel is '+str(total_parallel2_res)+' (degC/W)'

#Conductive Resistance in series
ListofResistance_series=[R1,R2,R6]
total_series_res=0
print'*********************************************************************************************************'
print'Below are the individual calculated resistance in series i.e. Foam,Plaster towards inner surface and Plaster towards outer surface, respectively:'
print'******'
for anyresistance in ListofResistance_series:
    L_anyresistance=anyresistance['Lenght']
    k_anyresistance=anyresistance['Conductivity']
    A_anyresistance=anyresistance['Area']
    Res_value=L_anyresistance/(k_anyresistance*A_anyresistance)
    total_series_res=total_series_res+Res_value
    name_resistanceS=anyresistance['name']
    print'The calculated Resistance of '+name_resistanceS+' is '+str(Res_value)+' (degC/W)'
    print'******'
print'So,The total sum of resistance in series is '+str(total_series_res)+' (degC/W)'

#Convective Resistance in series
ListofResistance_Conv_series=[Ri,Ro]
total_conv_series_res=0
print'************************************************************************************************'
print'Below are the individual calculated resistance in series of inner and outer surface respectively:'
print'******'
for anyresistance in ListofResistance_Conv_series:
    h_anyresistance=anyresistance['h']
    A_anyresistance=anyresistance['Area']
    Res_value=1/(h_anyresistance*A_anyresistance)
    total_conv_series_res=total_conv_series_res+Res_value
    name_resistanceConvS=anyresistance['name']
    print'The calculated Resistance of '+name_resistanceConvS+' is '+str(Res_value)+' (degC/W)'
    print'******'
print'So,The total sum of convective resistance in series is '+str(total_conv_series_res)+' (degC/W)'

R_Total=total_parallel_res+total_series_res+total_conv_series_res #Total Thermal Resistance

T0=20 #Indoor Temperature
T1=-10 #outdoor Temperature
W_Height=3 #Total Height of wall
W_Wide=5 #Total width of wall
A_total=W_Height*W_Wide #total area of wall

Q=(T0-T1)/R_Total #Heat Transfer through unit wall

QFinal=(Q*A_total)/0.25 #Total Heat Transfer
print'************************************************************************************************'
print'Finally,the total thermal resistance is '+str(R_Total) +'(degC/W)'+' and Total heat transfer across the wall is '+str(QFinal) +'(W)'


  