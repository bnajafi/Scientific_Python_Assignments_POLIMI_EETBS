#Assignment1
#Step 1
#Name:Shashwat Parsana

print'After compiling the given data: '

Kb=0.72 #conductivity of brick
Kp=0.22 #conductivity of plaster 
Kf=0.026 #conductivity of foam 

h1=10 #heat transfer coefficient of inner side
h2=25 #heat transfer coefficient of outer side

Lf=0.03 #Thickness of foam
Lp=0.02 #Thickness of plaster
Lb=0.16 #Thickness of brick

T0=20 #Indoor Temperature
T1=-10 #outdoor Temperature

W_Height=3 #Total Height of wall
W_Wide=5 #Total width of wall

Height=0.25 #Portion of Height of wall 
Lenght=1 #Assumed depth of wall

Hb=0.22 #Height of brick
Hbp=0.015 #Height of plaster over and below brick

A_total=W_Height*W_Wide #total area of wall
A0=Height*Lenght #area of unit wall

Ri=1/(h1*A0) ##Thermal Resistance of Indoor 
R1=Lf/(Kf*A0) #Thermal Resistance of Foam
R2=Lp/(Kp*A0) #Thermal Resistance of Plaster

R3=Lb/(Kb*Hb) #Thermal Resistance of Brick
R4=Lb/(Kp*Hbp) #Thermal Resistance of Plaster over brick
R5=R4 #Thermal Resistance of Plaster below brick

R6=R2 #Thermal Resistance of Plaster
Ro=1/(h2*A0) #Thermal Resistance of outdoor

R_total=Ri+R1+R2+((R3*R4)/(R4+(2*R3)))+R6+Ro #total thermal resistance

Q=(T0-T1)/R_total #Heat Transfer through unit wall

QFinal=(Q*A_total)/A0 #Total Heat Transfer

print'The total thermal resistance is '+str(R_total) +'(degC/W)'+' and Total heat transfer across the wall is '+str(QFinal) +'(W)'
