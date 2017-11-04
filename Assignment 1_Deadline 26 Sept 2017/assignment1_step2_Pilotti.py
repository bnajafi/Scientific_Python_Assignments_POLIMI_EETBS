# Example D - Heat Loss Through a Composite Wall 

# Data settings 

# Geometric parameters of the wall
W=float(raw_input('enter the total largeness of the wall in m: '))
H=float(raw_input('enter the total highness of the wall in m: '))

Lf=float(raw_input('enter the thickness of the foam layer in m: '))
Lp_horiz=float(raw_input('enter the orizontal thickness of the plaster layer in m: ')) #considering the same thickness in the both side
Lp_vert=float(raw_input('enter the vertical thickness of the plaster layer in m: '))   #considering the same thickness in the both side
Lb_horiz=float(raw_input('enter the orizontal thickness of the brick in m: '))
Lb_vert=float(raw_input('enter the vertical thickness of the brick in m: '))

# Conductivity coefficients
kf=float(raw_input('enter the conductivity of foam in W/m.K: '))
kp=float(raw_input('enter the conductivity of plaster in W/m.K: '))
kb=float(raw_input('enter the conductivity of brick in W/m.K: '))

# Convection heat transfer coefficients
hin=float(raw_input('enter the convection heat transfert coefficient of the inner side of the wall in W/m2: '))
hext=float(raw_input('enter the convection heat transfert coefficient of the outer side of the wall in W/m2: ')) 

# Temperatures
Tin=float(raw_input('enter the temperature inside the wall in K: '))
Tout=float(raw_input('enter the temperature outside the wall in K: '))


# Calculating the resistances
L_vert=Lp_vert+Lb_vert
A=L_vert*1  # area of a singol section considering a largeness of 1 m

Rin=1/(hin*A)
Rout=1/(hext*A)
R1=Lf/(A*kf)
R2=Lp_horiz/(A*kp)
R3=Lb_horiz/(kp*1*Lp_vert)
R4=Lb_horiz/(kb*1*Lb_vert)
R5=R3
R6=R2
 
# parallel 
R_eq=((1/R3)+(1/R4)+(1/R5))**-1

#total resistance of the wall section
Rtot=Rin+R1+R2+R_eq+R6+Rout

#Rate of heat transfer through the wall
Q_section=(Tin-Tout)/Rtot
Q_wall=Q_section*(H/L_vert)*W

print('The total thermal resistence of the wall section is: '+str(Rtot)+' K/W')
print('The rate of heat transfer through the wall is: '+str(Q_wall)+' W')
