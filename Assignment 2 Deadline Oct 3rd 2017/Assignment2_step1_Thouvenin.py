# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 15:45:39 2017

@author: edoua
"""

 #Rcond=[area,length, conductivity] 
Rf=[0.25,0.03,0.026]    #Rfoam          
Rp1=[0.25,0.02,0.22]    #Rplaster
Rp2=[0.25,0.02,0.22]
Rpc1=[0.015,0.16,0.22]
Rpc2=[0.015,0.16,0.22]
Rb=[0.22,0.16,0.72]
R1=[0.25,10]            #Rconv=[area,h]
R2=[0.25,20]

R =[Rf,Rp1,Rp2,Rpc1,Rpc2,Rb,R1,R2]      #list of all resistances
Rcondser=[Rf,Rp1,Rp2]                   #list of conduction resistances in serie
Rcondpara=[Rpc1,Rpc2,Rb]                #list of conduction resistances in parallel
Rconv=[R1,R2]                           #list of convection resistances

Tin = 20        #Interior temperature
Tout = -10      #Exterior temperature

valueRcondser = 0        #value of the sum of the resistance of conduction in serie
for anyRcondser in Rcondser :
    A_anyRcondser = anyRcondser[0]
    L_anyRcondser = anyRcondser[1]
    k_anyRcondser = anyRcondser[2]
    Res_anyRcondser = L_anyRcondser / (k_anyRcondser * A_anyRcondser)
    valueRcondser= valueRcondser + Res_anyRcondser
    
invvalueRcondpara = 0        #value of the sum of the resistance of conduction in parallel
for anyRcondpara in Rcondpara :
    A_anyRcondpara = anyRcondpara[0]
    L_anyRcondpara = anyRcondpara[1]
    k_anyRcondpara = anyRcondpara[2]
    Res_anyRcondpara = L_anyRcondpara / (k_anyRcondpara * A_anyRcondpara)
    invvalueRcondpara= invvalueRcondpara + 1 / Res_anyRcondpara    
valueRcondpara = 1/invvalueRcondpara
    

valueRconv = 0        #value of the sum of the resistance of convection in serie
for anyRconv in Rconv :
    A_anyRconv = anyRconv[0]
    h_anyRconv = anyRconv[1]
    Res_anyRconv = 1 / (h_anyRconv * A_anyRconv)
    valueRconv= valueRconv + Res_anyRconv


Rtot = valueRcondser + valueRcondpara + valueRconv
print "The value of the total resistance across the wall is: " + str(Rtot) + " °C/W"











