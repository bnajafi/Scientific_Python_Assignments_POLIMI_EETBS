#Assignment No. 1(Step2)(Date: 24.09.17)
#Debayan Paul

print("Please Enter all the values required for the calculation")

h1=float(raw_input("Please Enter the Convective Heat Transfer co-efficient on the inner side in W/m^2 degC: "))
h2=float(raw_input("Please Enter the Convective Heat Transfer co-efficient on the outer side in W/m^2 degC: "))
Kp=float(raw_input("Please Enter the Thermal conductivity of Plaster in W/m degC: "))
Kb=float(raw_input("Please Enter the Thermal conductivity of Brick in W/m degC: "))
Kf=float(raw_input("Please Enter the Thermal conductivity of Foam in W/m degC: ")) 
T1=float(raw_input("Please Enter the Indoor temperature in degC: "))
T2=float(raw_input("Please Enter the Outdoor temperature in degC: "))
d=float(raw_input("Please Enter the commom depth for every part of the unit in m: "))
l1=float(raw_input("Please Ener the length of indoor covective side in cm: "))
A1=l1*0.01*d #in m^2, Effective area of indoor heat convection
l2=float(raw_input("Please Ener the length of outdoor covective side in cm: "))
A2=l2*0.01*d #in m^2, Effective area of outdoor heat convection
lf=float(raw_input("Please Ener the length of foam in cm: "))
Af=lf*0.01*d #in m^2, Effective area of foam part
lp=float(raw_input("Please Ener the length of plaster in cm: "))
Ap=lp*0.01*d #in m^2, Effective area of both of the plaster side
lpc=float(raw_input("Please Ener the length of plaster ceiling side in cm: "))
Apc=lpc*0.01*d #in m^2, Effective area of both of the plaster ceiling side
lb=float(raw_input("Please Ener the length of brick in cm: "))
Ab=lb*0.01*d #in m^2, Effective area of brick part
Lf=float(raw_input("Please Ener the thickness of the foam in cm: "))
Lp=float(raw_input("Please Ener the thickness of the plaster in cm: "))
Lpc=float(raw_input("Please Ener the thickness of the plaster ceiling in cm: "))
Lb=float(raw_input("Please Ener the thickness of the brick in cm: "))
R1=1/(h1*A1) #in degC/W, Thermal resistance of outdoor convective part
R2=1/(h2*A2) #in degC/W, Thermal resistance of indoor convective part
Rf=(Lf*0.01)/(Kf*Af) #in degC/W, Thermal resistance of foam
Rp=(Lp*0.01)/(Kp*Ap) #in degC/W, Thermal resistance of both of the plaster side
Rpc=(Lpc*0.01)/(Kp*Apc) #in degC/W, Thermal resistance of both the plaster ceiling side
Rb=(Lb*0.01)/(Kb*Ab) #in degC/W, Thermal resistance of brick
Rparallel=1/(((1/Rpc)*2)+(1/Rb)) #in degC/W, as the both the plaster side and brick is in parallel connection
Rtotal=round((R1+R2+Rf+(2*Rp)+Rparallel),2) #in degC/W, The total thermal resistance of each block(unit)
Unit=(3*5)/0.25 #Total number of units
Qtotal=round((Unit*((T1-T2)/Rtotal)),2) #in Watt, Total heat transfer rate
print("The total effective thermal resistance is: "+str(Rtotal)+" degC/W")
print("The rate of heat transfer through the wall is "+str(Qtotal)+" Watt")


