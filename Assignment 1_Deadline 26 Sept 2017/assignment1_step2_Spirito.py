# -*- coding: utf-8 -*-
H_wall = float(raw_input('Enter the wall height in m')) #altezza del muro
W_wall = float(raw_input('Enter the wall width in m')) #spessore del muro
H_brick = float(raw_input('Enter the brick height in m')) #altezza del mattone
L_brick = float(raw_input('Enter the brick length in m')) #lunghezza del mattone
L_foam = float(raw_input('Enter the foam thickness in m')) #lunghezza del rigid foam
T_p1 = float(raw_input('Enter the lateral plaster thickness in m')) #spessore del plaster verticale
T_p2 = float(raw_input('Enter the top/bottom plaster thickness in m')) #spessore del plaster orizzontale

k_brick = float(raw_input('Enter the brick conductivity in W/mK')) #conduttività mattone
k_plaster = float(raw_input('Enter the plaster conductivity in W/mK')) #conduttività plaster
k_foam = float(raw_input('Enter the foam conductivity in W/mK')) #conduttività foam

h_i = float(raw_input('Enter the convection heat transfer coefficient of the inner side in W/Km^2')) #coeff. convettivo interno
h_o = float(raw_input('Enter the convection heat transfer coefficient of the outer side in W/Km^2')) #coeff. convettivo esterno
T_i = float(raw_input('Enter the temperature of the inner side in degC')) #temp. interna
T_o = float(raw_input('Enter the temperature of the outer side in degC')) #temp. esterna

A_wall = (H_wall*W_wall) #area muro
A_unit = ((H_brick+T_p2*2)*W_wall) #area unità considerata
A_brick = (H_brick*W_wall) #area mattone
A_p = (T_p2*W_wall) #area plaster orizzontale

Ri = 1/(h_i*A_unit) #Rconv interno
Ro = 1/(h_o*A_unit) #Rconv esterno
Rf = L_foam/(k_foam*A_unit) #Rcond foam
Rp1 = T_p1/(k_plaster*A_unit) #Rcond plaster verticale
Rp2 = L_brick/(k_plaster*A_p) #Rcond plaster orizzontale
R_b = L_brick/(k_brick*A_brick) #Rcond mattone

R_parallel = (1/R_b)+(1/Rp2*2)
R_tot= R_parallel+Ri+Ro+Rf+Rp1*2

Q_unit = (T_i-T_o)/R_tot #potenza termica trasmessa attraverso l'unità considerata
Q_wall = Q_unit*(A_wall/A_unit) #potenza termica trasmessa attraverso il muro

print 'The total thermal resistance is '+str(R_tot)+ ' (degC/W)'
print 'The heat transfer rate through the wall is '+str(Q_wall)+ ' (W)'
