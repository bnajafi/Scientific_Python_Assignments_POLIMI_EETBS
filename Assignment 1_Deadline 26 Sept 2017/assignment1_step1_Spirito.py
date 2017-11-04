# -*- coding: utf-8 -*-
H_wall = 3     #altezza del muro
W_wall = 5     #spessore del muro
H_brick = 0.22   #altezza del mattone
L_brick = 0.16  #lunghezza del mattone
L_foam =  0.03  #lunghezza del rigid foam
T_p1 = 0.02  #spessore del plaster verticale
T_p2 = 0.015 #spessore del plaster orizzontale

k_brick = 0.72  #conduttività mattone
k_plaster = 0.22 #conduttività plaster
k_foam = 0.026  #conduttività foam

h_i = 10 #coeff. convettivo interno
h_o = 25 #coeff. convettivo esterno
T_i = 20 #temp. interna
T_o = -10 #temp. esterna

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

print 'The total thermal resistance is '+str(R_tot)+ ' degC/W'
print 'The heat transfer rate through the wall is '+str(Q_wall)+ ' W'
