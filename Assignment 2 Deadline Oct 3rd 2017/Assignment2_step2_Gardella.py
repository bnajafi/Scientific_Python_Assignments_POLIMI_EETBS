# -*- coding: utf-8 -*-
#Temperatures

T1=20 
T2=-10

#Areas

Awall=15
Aelement=0.25

#Defining resistances as dictionaries

R0={"Type":"Convective","Name":"Interior","Area":0.25,"Conv.Coefficient":10,"Value":0}
R7={"Type":"Convective","Name":"Exterior","Area":0.25,"Conv.Coefficient":25,"Value":0}

R1={"Type":"Conductive","Name":"Foam","Area":0.25,"Thickness":0.03,"Cond.Coefficient":0.026,"Value":0}
R2={"Type":"Conductive","Name":"Plaster1","Area":0.25,"Thickness":0.02,"Cond.Coefficient":0.22,"Value":0}
R3={"Type":"Conductive","Name":"Plaster2","Area":0.015,"Thickness":0.16,"Cond.Coefficient":0.22,"Value":0}
R4={"Type":"Conductive","Name":"Brick","Area":0.22,"Thickness":0.16,"Cond.Coefficient":0.72,"Value":0}
R5={"Type":"Conductive","Name":"Plaster3","Area":0.015,"Thickness":0.16,"Cond.Coefficient":0.22,"Value":0}
R6={"Type":"Conductive","Name":"Plaster4","Area":0.25,"Thickness":0.02,"Cond.Coefficient":0.22,"Value":0}

#Defining list of resistances

Rcond=[R1,R2,R3,R4,R5,R6]# All conductive resistances
Rpar=[R3,R4,R5]  # Conductive resistances in parallel
Rser=[R1,R2,R6] # Conductive resistances in series
Rconv=[R0,R7] #Convective resistances


#CALCULATIONS

#All conductive resistances

for anyresistance in Rcond:
    L_anyresistance=anyresistance["Thickness"]
    A_anyresistance=anyresistance["Area"]
    k_anyresistance=anyresistance["Cond.Coefficient"]
    
    ResVal=L_anyresistance/(A_anyresistance*k_anyresistance)
    
    anyresistance["Value"]=ResVal #Assign the calculated value in the dictionary

#Conductive resistances in parallel

TotInv=0

for anypar in Rpar:
    ResParVal=anypar["Value"]
    InvPar=1/ResParVal
    TotInv=TotInv+InvPar

ResParTotVal=1/TotInv

Rpar.append(ResParTotVal)#Add the equivalent value of the resistances in parallel in the correspondig list 

#Conductive resistances in series

TotSer=0

for anyser in Rser:
    ResSerVal=anyser["Value"]
    TotSer=TotSer+ResSerVal
    
Rser.append(TotSer)

#Convective resistances

TotConv=0
for anyresistance in Rconv:
    A_anyresistance=anyresistance["Area"]
    h_anyresistance=anyresistance["Conv.Coefficient"]
    
    ResVal=1/(A_anyresistance*h_anyresistance)
    TotConv=TotConv+ResVal
    anyresistance["Value"]=ResVal
  
Rconv.append(TotConv)

#Total Resistance of the single element

Rtot=Rconv[-1]+Rser[-1]+Rpar[-1] #Recall the values from conductive and convective lists 

#Heat flux of the single element

Q=(T1-T2)/Rtot

#Heat flux of the entire wall

Qwall=Q*(Awall/Aelement)

print"The total resistance is "+str(Rtot)+" °C/W"
print"The heat flux trough the wall is "+str(Qwall)+" W"
