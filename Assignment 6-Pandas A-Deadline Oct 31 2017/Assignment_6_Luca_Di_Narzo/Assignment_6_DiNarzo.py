# -*- coding: utf-8 -*-
import pandas as pd

T1= 20 #Indoor temperature
T2= -10 #Outdoor temperatureL1= 0.03 #Thickness of foam
H=0.25 #Total heigth

#Assuming the width equal to 1m

#Defining all the resistences' caracteristics
R_conv_1=['conv','series',10,None,None,0.25,0]
R_conv_2=['conv','series',25,None,None,0.25,0]
R1_series=['cond','series',None,0.026,0.03,0.25,0]
R2_series=['cond','series',None,0.22,0.04,0.25,0]
R1_parallel=['cond','parall',None,0.22,0.16,0.015,0]
R2_parallel=['cond','parall',None,0.22,0.16,0.015,0]
R3_parallel=['cond','parall',None,0.72,0.16,0.22,0]

#Creating the table
Index_names=['R_conv1','R_conv2','R1_series','R2_series','R1_parallel','R2_parallel','R3_parallel']
Column_names=['Type','Configuration','H','K','L','A','R_value']

resistances_DF=pd.DataFrame([R_conv_1,R_conv_2,R1_series,R2_series,R1_parallel,R2_parallel,R3_parallel],index=Index_names,columns=Column_names)

#Calculating the resistence value
resistances_DF['R_value'][resistances_DF['Type']=='conv']=1/(resistances_DF['H'][resistances_DF['Type']=='conv']*resistances_DF['A'][resistances_DF['Type']=='conv'])
resistances_DF['R_value'][resistances_DF['Type']=='cond']=resistances_DF['L'][resistances_DF['Type']=='cond']/(resistances_DF['K'][resistances_DF['Type']=='cond']*resistances_DF['A'][resistances_DF['Type']=='cond'])

#Calculating the total resistance
R_tot_series=resistances_DF['R_value'][resistances_DF['Configuration']=='series'].sum()
R_parallel_recip=1/resistances_DF['R_value'][resistances_DF['Configuration']=='parall']
R_parallel_tot=1/R_parallel_recip.sum()
R_TOT=R_tot_series+R_parallel_tot

print ('The total resistence is ') + str(R_TOT) + (' °C/W')
print ' '

#Calculating the Q-Value
Q=(T1-T2)/R_TOT #Q of the unit area
print ('The rate of heat transfer through the wall per unit area is ') +str(Q) + (' W')
print ' '
Htot=3 #Total height
Ltot=5 #Total width
print ' '
Qtot=Q*Ltot*Htot/H #Q total
print ('The total rate of heat transfer through the wall is ') +str(Qtot) + (' W') 