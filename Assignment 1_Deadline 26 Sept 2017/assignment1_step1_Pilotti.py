# Example D - Heat Loss Through a Composite Wall 


# Data settings 

# Geometric parameters of the wall
W=5
H=3

Lf=0.03
Lp_horiz=0.02 #considering the same thickness in the both side
Lp_vert=0.015   #considering the same thickness in the both side
Lb_horiz=0.16
Lb_vert=0.22

# Conductivity coefficients
kf=0.026
kp=0.22
kb=0.72

# Convection heat transfer coefficients
hin=10
hext=25
# Temperatures
Tin=20
Tout=-10


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

print('The total thermal resistence of the wall section is: '+str(Rtot)+' K/W');
print('The rate of heat transfer through the wall is: '+str(Q_wall)+' W')
