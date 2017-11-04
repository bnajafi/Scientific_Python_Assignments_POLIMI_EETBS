# -*- coding: utf-8 -*-
#Temperatures

T1=20 
T2=-10

#Areas

Awall=15
Aelement=0.25

#Defining resistances as a list 

R0=["Conv","Interior",0.25,10,0] #(Type,Side,Area,Conv. coefficient,Value=0)
R7=["Conv","Exterior",0.25,25,0]

R1=["Cond","Foam",0.25,0.03,0.026,0] #(Type,Material,Area,Thickness,Conductivity coefficient,Value=0)
R2=["Cond","Plaster",0.25,0.02,0.22,0]
R3=["Cond","Plaster",0.015,0.16,0.22,0]
R4=["Cond","Brick",0.22,0.16,0.72,0]
R5=["Cond","Plaster",0.015,0.16,0.22,0]
R6=["Cond","Plaster",0.25,0.02,0.22,0]

#Defining list of resistances

Rcond=[R1,R2,R3,R4,R5,R6]# All conductive resistances
Rpar=[R3,R4,R5]  # Conductive resistances in parallel
Rser=[R1,R2,Rpar,R6] # Conductive resistances in series
Rconv=[R0,R7] #Convective resistances


#CALCULATIONS

#All conductive resistances

for anyresistance in Rcond:
    L_anyresistance=anyresistance[3]
    A_anyresistance=anyresistance[2]
    k_anyresistance=anyresistance[4]
    
    ResVal=L_anyresistance/(A_anyresistance*k_anyresistance)
    
    anyresistance[-1]=ResVal #Assign the calculated value in his index position in the list

#Conductive resistances in parallel

TotInv=0

for anypar in Rpar:
    ResParVal=anypar[-1]
    InvPar=1/ResParVal
    TotInv=TotInv+InvPar

ResParTotVal=1/TotInv

Rpar.append(ResParTotVal)#Add the equivalent value of the resistances in parallel in the correspondig list 

#Conductive resistances in series

TotSer=0

for anyser in Rser:
    ResSerVal=anyser[-1]
    TotSer=TotSer+ResSerVal
    
Rser.append(TotSer)

#Convective resistances

TotConv=0
for anyresistance in Rconv:
    A_anyresistance=anyresistance[2]
    h_anyresistance=anyresistance[3]
    
    ResVal=1/(A_anyresistance*h_anyresistance)
    TotConv=TotConv+ResVal
    anyresistance[-1]=ResVal
  
Rconv.append(TotConv)

#Total Resistance of the single element

Rtot=Rconv[-1]+Rser[-1] #Recall the values from conductive and convective lists 

#Heat flux of the single element

Q=(T1-T2)/Rtot

#Heat flux of the entire wall

Qwall=Q*(Awall/Aelement)

print"The total resistance is "+str(Rtot)+" °C/W"
print"The heat flux trough the wall is "+str(Qwall)+" W"
