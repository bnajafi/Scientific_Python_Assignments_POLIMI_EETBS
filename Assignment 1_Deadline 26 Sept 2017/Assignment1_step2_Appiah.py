# Thermal Conduction and Convection Heat Transfer Example D

H_wall = float(raw_input('Enter height of wall in m '))    
W_wall = float(raw_input('Enter width of wall in m '))    
A_wall = (H_wall*W_wall) #area of wall

H_brick = float(raw_input('Enter the cross section of brick in m '))  #cross section of brick
L_brick = float(raw_input('Enter the length brick in m '))  #length of brick
L_foam =  float(raw_input('Enter the length rigidd Foam in m '))  #length of rigid foam
T_p1 = float(raw_input('Enter the thickness of vertical plaster in m '))  #thickness of vertical plaster
T_p2 = float(raw_input('Enter the thickness of horizontal plaster in m ')) #thickness of horizontal plaster

A_unit = ((H_brick+T_p2*2)*W_wall) #unit area
A_brick = (H_brick*W_wall) #area of brick
A_hp = (T_p2*W_wall) #area of horizontal plaster

k_brick = float(raw_input('Enter the conductivity of the brick in W/mK '))  
k_plaster = float(raw_input('Enter the conductivity of plaster in W/mK '))  
k_foam = float(raw_input('Enter the conductivity of foam in W/mK '))  
h_1 = float(raw_input('Enter the inner convection heat transfer coefficient in W/Km^2 ')) 
h_2 = float(raw_input('Enter the external convection heat transfer coefficient in W/Km^2 ')) 
T_1 = float(raw_input('Enter the indoor temperature in degC ')) 
T_2 = float(raw_input('Enter the outdoor temperature in degC ')) 

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
