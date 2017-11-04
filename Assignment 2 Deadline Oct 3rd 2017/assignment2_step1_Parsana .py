#Assignment 2
#Name:Shashwat Parsana
#STEP:1

Ri=[10,0.25] #h=0,A=1,Inner wall
R1=[0.03,0.026,0.25] #L=0,k=1,A=2,Foam
R2=[0.02,0.22,0.25] #L=0,k=1,A=2,Plaster towards inner surface
R3=[0.16,0.22,0.015] #L=0,k=1,A=2,Plaster above brick
R4=[0.16,0.72,0.22] ##L=0,k=1,A=2,Brick
R5=[0.16,0.22,0.015] #Plaster below brick
R6=[0.02,0.22,0.25] #Plaster towards outer surface
Ro=[25,0.25] ##h=0,A=1,Outer wall

#Conductive Resistance in Parallel
ListofResistance_parallel=[R3,R4,R5]
total_parallel_res=0
print'*********************************************************************************************************'
print'Below are the individual calculated resistance in parallel i.e. Plaster above brick,Brick and Plaster below brick, respectively:'
print'******'
for anyresistance in ListofResistance_parallel:
    L_anyresistance=anyresistance[0]
    k_anyresistance=anyresistance[1]
    A_anyresistance=anyresistance[2]
    Res_value=L_anyresistance/(k_anyresistance*A_anyresistance)
    total_parallel_res=total_parallel_res+(1/Res_value)
    total_parallel2_res=1/total_parallel_res
    print'The calculated Resistance is '+str(Res_value) +' (degC/W)'
    print'******'
print'So,The total sum of resistance in Parallel is '+str(total_parallel2_res)+' (degC/W)'

#Conductive Resistance in series
ListofResistance_series=[R1,R2,R6]
total_series_res=0
print'*********************************************************************************************************'
print'Below are the individual calculated resistance in series i.e. Foam,Plaster towards inner surface and Plaster towards outer surface, respectively:'
print'******'
for anyresistance in ListofResistance_series:
    L_anyresistance=anyresistance[0]
    k_anyresistance=anyresistance[1]
    A_anyresistance=anyresistance[2]
    Res_value=L_anyresistance/(k_anyresistance*A_anyresistance)
    total_series_res=total_series_res+Res_value
    print'The calculated Resistance is '+str(Res_value)+' (degC/W)'
    print'******'
print'So,The total sum of resistance in series is '+str(total_series_res)+' (degC/W)'

#Convective Resistance in series
ListofResistance_Conv_series=[Ri,Ro]
total_conv_series_res=0
print'************************************************************************************************'
print'Below are the individual calculated resistance in series of inner and outer surface respectively:'
print'******'
for anyresistance in ListofResistance_Conv_series:
    h_anyresistance=anyresistance[0]
    A_anyresistance=anyresistance[1]
    Res_value=1/(h_anyresistance*A_anyresistance)
    total_conv_series_res=total_conv_series_res+Res_value
    print'The calculated Resistance is '+str(Res_value)+' (degC/W)'
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


  