# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.1 (Step1) Date: 24/09/2017
#One dimensional problem:
#Example D: Heat loss through a composite wall
#Wall:
H_w =5.0 #high of wall
W_w =3.0 #wide of wall
A_w= H_w*W_w #area of wall

#Temperature:
Tin= 20 #Indoor temperature of wall in degC
Tout= -10 #Outdoor temperature of wall in degC

#Foam:
L_f = 0.03 #length of foam in m
k_f =0.026 #coefficient of thermal conductivity of foam in W/mdegC
H_f =0.015+0.015+0.22  #height of foam in m
A_f = H_f*1 #cross-sectional area of foam in m2

#Plaster:
L_p = 0.02 #length of plaster in m
k_p =0.22 #coefficient of thermal conductivity of plaster in W/mdegC
H_p =0.22+0.015+0.015 #height of plaster in m
A_p =H_p*1 #cross-sectional area of plaster in m2

#Brick:
L_b = 0.16 #length of brick in m
k_b =0.72 #coefficient of thermal conductivity of brick in W/mdegC
H_b =0.22 #height of brick in m
A_b =H_b*1 #cross-sectional area of brick in m2

#Brick-plaster region:
L_bp= 0.16 #length of brick-plaster region in m
H_bp=0.015 # height of brick-plaster region in m
A_bp=H_bp*1 #cross-sectional area of brick-plaster region in m2

#Convection coefficient:
h1= 10.0 #convection heat transfer coefficient on the inner side in W/m2degC
h2 = 25.0 #convection heat transfer coefficient on the outer side in W/m2degC

#Calculation of resistances:
R_1= 1/(h1*A_f) # convection resistance on the inner side of the wall in (degC/W)
R_2= 1/(h2*A_f)# convection resistance on the outer side of the wall in (degC/W)
R_f= L_f/(k_f*A_f) # conductive resistance in foam in (degC/W)
R_p1=L_p/(k_p*A_p) # conductive resistance in plaster on the inner side in (degC/W)
R_b= L_b/(k_b*A_b) # conductive resistance in brick in (degC/W)
R_bp1=L_bp/(k_p*A_bp)  # conductive resistance in brick-plaster region in (degC/W)
R_bp2=L_bp/(k_p*A_bp)  # conductive resistance in brick-plaster region in (degC/W)
R_p2=L_p/(k_p*A_p)  # conductive resistance in plaster on the outer side in (degC/W)

#Equivalent parallel resistance between brick and two brick-plaster region:
R_par = 1/((1/R_b) +(1/R_bp1) +(1/R_bp2)) # in (degC/W)
#Total resistance:
R_total= R_1 + R_f + R_p1 + R_par + R_p2 + R_2 # in (degC/W)
print "total resistance through the wall is "+str(R_total)+" degC/Watt"

Q_t = (Tin-Tout)/R_total # total heat transfer through the wall per unit width in Watt
print "total heat transfer through the wall per unit width is "+str(Q_t)+" Watt"

Q_total = Q_t*(A_w/A_f) # total heat transfer through the wall in Watt
print "the total heat transfer through the wall is "+str(Q_total)+" Watt "






 
