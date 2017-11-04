# Thermal Conduction and Convection Heat Transfer Example D

H_wall = 3     #height of wall
W_wall = 5     #width of wall
A_wall = (H_wall*W_wall) #area of wall

H_brick = 0.22   #cross section of brick
L_brick = 0.16  #length of brick
L_foam =  0.03  #length of rigid foam
T_p1 = 0.02  #thickness of vertical plaster
T_p2 = 0.015 #thickness of horizontal plaster

A_unit = ((H_brick+T_p2*2)*W_wall) #unit area
A_brick = (H_brick*W_wall) #area of brick
A_hp = (T_p2*W_wall) #area of horizontal plaster

k_brick = 0.72  #conductivity of brick
k_plaster = 0.22 #conductivity of plaster
k_foam = 0.026  #conductivity of foam
h_1 = 10 # inner convection heat transfer coefficient
h_2 = 25 #external convection heat transfer coefficient
T_1 = 20 #indoor temperature
T_2 = -10 #outdoor temperature

R_1 = 1/(h_1 * A_unit) #convection resistance of inner
R_2 = 1/(h_2 * A_unit) #convection resistance of external
R_f = L_foam/(k_foam * A_unit) #conductive resistance of foam
R_b = L_brick/(k_brick * A_brick) #conductive resistance of brick
R_p1 = T_p1/(k_plaster * A_unit) #conductive resistance of vertical plaster
R_p2 = L_brick/(k_plaster * A_hp) #conductive resistance of horizontal plaster 
R_parallel = (1 / R_b)+(1 / R_p2 * 2)
R_tot= R_parallel + R_1 + R_2 + R_f + (R_p1*2)

Q_unit = (T_1 - T_2) / R_tot #total heat transfer through the wall per unit width [W]
Q_wall = Q_unit * (A_wall/A_unit) #total heat transfer through the wall [W]

print 'The total thermal resistance is '+str(R_tot)+ ' degC/W'
print 'The rate of heat transfer through the wall is '+str(Q_wall)+ ' W'
