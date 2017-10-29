#EX 3
#step2

#ambiental conditions (o=outdoor,i=indoor)
To=-10
Ti=20

#coefficients and geometric dimensions 

#convection coeff.
hi=float(raw_input("please enter indoor convective coeff. (W/m2): "))
ho=float(raw_input("please enter outdoor convective coeff. (W/m2): "))

#wall dimensions
L=5
H=3
A_tot=H*L

#section dimensions
l=1
h=0.25
a_1=l*h
a_bricks=0.22*1
a_3=0.015*1

#conduction coeff.
k_bricks=float(raw_input("brick's conductivity (W/m) : "))
k_foam=float(raw_input("foam's conductivity (W/m) : "))
k_plaster=float(raw_input("plaster's conductivity (W/m) : "))

#thickness
t_bricks=0.16
t_foam=0.03
t_plaster=0.02

#conductive resistances
R_bricks=t_bricks/(k_bricks*a_bricks)
R_foam=t_foam/(k_foam*a_1)
R_plaster1=t_plaster/(k_plaster*a_1)
R_plaster2=t_bricks/(k_plaster*a_3)

#convective resistances
R_conv_o=1/(ho*a_1)
R_conv_i=1/(hi*a_1)

#total resistance calculation
R_parallel=1/((1/R_bricks)+(1/R_plaster2)+(1/R_plaster2))
R_tot=R_conv_o+R_conv_i+R_parallel+2*R_plaster1+R_foam

#heat transfer calculation
q=(Ti-To)/(R_tot*0.25)
Q=q*(A_tot)

print "\nthe total thermal Resistance is: " +str(R_tot)+ " degC/W \n"
print "the total heat transferof the considered wall is: "+str(Q)+ " W \n"