#Assignment1
#Step 2
#Name:Shashwat Parsana

print'Hello,Please provide following asked required data to get Total thermal Resistance and Total Heat Transfer across the wall: '

Kb=float(raw_input('Conductivity of the brick in (W/m*degC) '))
Kp=float(raw_input('Conductivity of the plaster in (W/m*degC) '))
Kf=float(raw_input('Conductivity of the foam in (W/m*degC) '))

h1=float(raw_input('Heat transfer coefficient of inner side in (W/m2*degC) '))
h2=float(raw_input('Heat transfer coefficient of outer side in (W/m2*degC) '))

Lf=float(raw_input('Thickness of foam in (m) '))
Lp=float(raw_input('Thickness of plaster in (m) '))
Lb=float(raw_input('Thickness of brick in (m) '))

T0=float(raw_input('What is the Indoor Temperature in (degC)?'))
T1=float(raw_input('What is the Outdoor Temperature in (degC)?'))

W_Height=float(raw_input('Total height of the wall in (m) '))
W_Wide=float(raw_input('Total width of the wall in (m) '))

Height=0.25 #Unit Portion of Height of wall 
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

print'Thank you!So the total thermal resistance is '+str(R_total) +'(degC/W)'+' and Total heat transfer across the wall is '+str(QFinal) +'(W)'
