B = 1 # for unit width
A_wall= 3.0*5.0

T1 = 20# Indoor temp of wall in K
T2 =-10.0  # outdoor temp of wall in K

L_f = 0.03 #the length of form in m 
k_f =0.026 # thermal conductivity of foam in W/m.K
H_f =0.25  # height of foam in m
A_f =H_f*B # cross-sectional area of foam in m2

L_p = 0.02 # length of plaster in  m
k_p =0.22 # thermal conductivity of plaster in W/m.K
H_p =0.25 #height of plaster in m
A_p =H_p*B # cross-sectional area of plaster in m2

L_b = 0.16 #length of brick of form in m
k_b =0.72# thermal conductivity of brick in W/m.K
H_b =0.22 #  height of brick in m
A_b =H_b*B #cross-sectional area of brick in m2

L_bp= 0.16 #length of brick- plaster in m
H_bp=0.015 # height of brick-plaster region in m
A_bp=H_bp*B# cross-sectional area of brick-plaster region in m2

h1 = 10.0 # convection heat transfer coefficient on the inner side in W/m2.K
h2 = 25.0 # convection heat transfer coefficient on the outer side in W/m2.K

R_0= 1/(h1*A_f) # convection resistance on the inner side of the wall in (K/W)
R_f= L_f/(k_f*A_f) # conductive resistance in foam in (K/W)
R_p1=L_p/(k_p*A_p) # conductive resistance in plaster on the inner side in (K/W)
R_b= L_b/(k_b*A_b) # conductive resistance in brick in (K/W)
R_bp1=L_bp/(k_p*A_bp) # conductive resistance in brick-plaster region in (K/W)
R_bp2=L_bp/(k_p*A_bp)# conductive resistance in brick-plaster region in (K/W)
R_p2=L_p/(k_p*A_p)# conductive resistance in plaster on the outer side in (K/W)
R_00= 1/(h2*A_f)# convection resistance on the outer side of the wall in (K/W)

R_pr = 1/((1/R_b) +(1/R_bp1) +(1/R_bp2)) # equivalent resistance for all the parallelly arranged resistances in (K/W)

R_total= R_0 + R_f + R_p1 + R_pr + R_p2 + R_00 # total resistance in (K/W)

Q_t =  (T1-T2)/R_total # total heat transfer through the wall per unit width in W
Q_total = Q_t*(A_wall/A_f) # total heat transfer through the wall in W

print "total resistance through the wall is " +str(R_total)+  "   K/W" 
print "total heat transfer through the wall per unit width is " +str(Q_t)+ "   W"
print "the total heat transfer through the wall is " + str(Q_total)+  "   W "









