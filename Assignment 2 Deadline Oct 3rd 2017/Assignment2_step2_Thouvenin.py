# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 18:18:27 2017

@author: edoua
"""

 #Rcond=[area,length, conductivity] 
Rf={"area":0.25,"length":0.03,"k":0.026}    #Rfoam          
Rp1={"area":0.25,"length":0.02,"k":0.22}    #Rplaster
Rp2={"area":0.25,"length":0.02,"k":0.22}
Rpc1={"area":0.015,"length":0.16,"k":0.22}
Rpc2={"area":0.015,"length":0.16,"k":0.22}
Rb={"area":0.22,"length":0.16,"k":0.72}
R1={"area":0.25,"h":10}            #Rconv=[area,h]
R2={"area":0.25,"h":20}

R =[Rf,Rp1,Rp2,Rpc1,Rpc2,Rb,R1,R2]      #list of all resistances
Rcondser=[Rf,Rp1,Rp2]                   #list of conduction resistances in serie
Rcondpara=[Rpc1,Rpc2,Rb]                #list of conduction resistances in parallel
Rconv=[R1,R2]                           #list of convection resistances

valueRcondser = 0        #value of the sum of the resistance of conduction in serie
for anyRcondser in Rcondser :
    A_anyRcondser = anyRcondser["area"]
    L_anyRcondser = anyRcondser["length"]
    k_anyRcondser = anyRcondser["k"]
    Res_anyRcondser = L_anyRcondser / (k_anyRcondser * A_anyRcondser)
    valueRcondser= valueRcondser + Res_anyRcondser
    
invvalueRcondpara = 0        #inverse of the value of the sum of the resistance of conduction in parallel
for anyRcondpara in Rcondpara :
    A_anyRcondpara = anyRcondpara["area"]
    L_anyRcondpara = anyRcondpara["length"]
    k_anyRcondpara = anyRcondpara["k"]
    Res_anyRcondpara = L_anyRcondpara / (k_anyRcondpara * A_anyRcondpara)
    invvalueRcondpara= invvalueRcondpara + 1 / Res_anyRcondpara    
valueRcondpara = 1/invvalueRcondpara
    

valueRconv = 0        #value of the sum of the resistance of convection in serie
for anyRconv in Rconv :
    A_anyRconv = anyRconv["area"]
    h_anyRconv = anyRconv["h"]
    Res_anyRconv = 1 / (h_anyRconv * A_anyRconv)
    valueRconv= valueRconv + Res_anyRconv


Rtot = valueRcondser + valueRcondpara + valueRconv
print "The value of the total resistance across the wall is: " + str(Rtot) + " °C/W"

