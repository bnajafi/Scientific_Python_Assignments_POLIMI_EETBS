#Assignment No. 1(Step1)(Date: 24.09.17)
#Debayan Paul


h1=10 #in W/m^2 degC, Convective Heat Transfer co-efficient on the inner side
h2=25 #in W/m^2 degC, Convective Heat Transfer co-efficient on the outer side
Kp=0.22 #in W/m degC, Thermal conductivity of Plaster
Kb=0.72 #in W/m degC, Thermal conductivity of Brick
Kf=0.026 #in W/m degC, Thermal conductivity of Foam
T1=20 #in degC, Indoor temperature
T2=-10 #in degC, Outdoor temperature
A1=(1.5+1.5+22)*0.01*1 #in m^2, Effective area of indoor heat convection
A2=(1.5+1.5+22)*0.01*1 #in m^2, Effective area of outdoor heat convection
Af=(1.5+1.5+22)*0.01*1 #in m^2, Effective area of foam part
Ap=(1.5+1.5+22)*0.01*1 #in m^2, Effective area of both of the plaster side
Apc=1.5*0.01*1 #in m^2, Effective area of both of the plaster ceiling side
Ab=22*0.01*1 #in m^2, Effective area of brick part
Lf=3*0.01 #in m, Thickness of foam 
Lp=2*0.01 #in m, Thickness of both of the plaster side 
Lpc=16*0.01 #in m, Thickness of both of the plaster ceiling side
Lb=16*0.01 #in m, Thickness of brick
R1=1/(h1*A1) #in degC/W, Thermal resistance of indoor convective part
R2=1/(h2*A2) #in degC/W, Thermal resistance of outdoor convective part
Rf=Lf/(Kf*Af) #in degC/W, Thermal resistance of foam
Rp=Lp/(Kp*Ap) #in degC/W, Thermal resistance of both of the plaster side
Rpc=Lpc/(Kp*Apc) #in degC/W, Thermal resistance of both the plaster ceiling side
Rb=Lb/(Kb*Ab) #in degC/W, Thermal resistance of brick
Rparallel=1/(((1/Rpc)*2)+(1/Rb)) #in degC/W, as the both the plaster side and brick is in parallel connection
Rtotal=round((R1+R2+Rf+(2*Rp)+Rparallel),2) #in degC/W, The total thermal resistance of each block(unit)
Unit=(3*5)/0.25 #Total number of units
Qtotal=round((Unit*((T1-T2)/Rtotal)),2) #in Watt, Total heat transfer rate
print("The total effective thermal resistance is: "+str(Rtotal)+" degC/W")
print("The rate of heat transfer through the wall is "+str(Qtotal)+" Watt")


