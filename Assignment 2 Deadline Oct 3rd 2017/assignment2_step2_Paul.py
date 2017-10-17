#*****Areas are pre-calculated for ease, all units are in SI******
Rci={"h":10,"Area":0.25}                         #Defining Convective resistance on the inner side as a dictionary
Rco={"h":25,"Area":0.25}                         #Defining Convective resistance on the outer side as a dictionary
Rf={"Thickness":0.03,"k":0.026,"Area":0.25}      #Defining Conducive resistance of foam as a dictionary
Rp1={"Thickness":0.02,"k":0.22,"Area":0.25}      #Defining Conductive resistance of Plaster side1 as a dictionary
Rp2={"Thickness":0.02,"k":0.22,"Area":0.25}      #Defining Conductive resistance of Plaster side2 as a dictionary
Rpc1={"Thickness":0.16,"k":0.22,"Area":0.015}    #Defining Conductive resistance of Plaster ceilingside1 as a dictionary
Rpc2={"Thickness":0.16,"k":0.22,"Area":0.015}    #Defining Conductive resistance of Plaster ceilingside2 as a dictionary
Rb={"Thickness":0.16,"k":0.72,"Area":0.22}       #Defining Conductive resistance of Brick as a dictionary
ConvReS=[Rci,Rco]                                #Defining covective resistances in series as a list where list items are a dictionary
CondReS=[Rf,Rp1,Rp2]                             #Defining coductive resistances in series as a list where list items are a dictionary
CondReP=[Rpc1,Rpc2,Rb]                           #Defining covective resistances in parallel as a list where list items are a dictionary
TotalConvReS=0                                   #Intializing total value of convective resistances as zero
TotalCondReS=0                                   #Intializing total value of conductive resistances in series as zero
TotalCondReP=0                                   #Intializing total value of conductive resistances in parallel as zero
for r in range(len(ConvReS)):
    TotalConvReS+=1/(ConvReS[r]["h"]*ConvReS[r]["Area"])                                       #Calculating the total resistance value of convective resistances in series   
for p in range(len(CondReS)):
    TotalCondReS+=CondReS[p]["Thickness"]/(CondReS[p]["k"]*CondReS[p]["Area"])                 #Calculating the total resistance value of conductive resistances in series    
for s in range(len(CondReP)):
    TotalCondReP+=1/((CondReP[s]["Thickness"]/(CondReP[s]["k"]*CondReP[s]["Area"])))           #Calculating the total resistance value of conductive resistances in parallel    
TotalCondReP=1/TotalCondReP                                                                    #Inversing the value for parallel resistances and assigning again to the old variable
TotalRes=round((TotalConvReS+TotalCondReS+TotalCondReP ),2)                                    #Calculating the effective total resistance value
T1=273+20                                                                                      #in K, Indoor temperature
T2=273-10                                                                                      #in K, Outdoor temperature
Unit=(3*5)/0.25                                                                                #Total number of units
Qtotal=int(Unit*((T1-T2)/TotalRes))                                                            #in Watt, Total heat transfer rate
print("The total effective thermal resistance is: "+str(TotalRes)+" degK/W")                  
print("The rate of heat transfer through the wall is "+str(Qtotal)+" Watt")