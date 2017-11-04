#EXERCISE 1, step 1
#parameters inserction
h_tot=3
h_brick=0.25
h_plaster=0.015

width_tot=5

L_foam=0.03
L_plaster=0.02
L_brick=0.16

Area_tot=h_tot*width_tot
Area_foam=0.25*1
Area_plaster=0.25*1
Area_plaster_lateral=0.015*1
Area_brick=0.22*1
tot_bricks=60

T_in=20
T_out=-10

h_plaster=0.015
h_brick=0.22
h_foam=0.25

h_int=10
h_ext=25

k_foam=0.026
k_brick=0.72
k_plaster=0.22

#CALCULATIONS
#Here there are the simpliest resistances
R_1=1/(h_int*Area_foam)
R_foam=L_foam/(k_foam*Area_foam)
R_plaster=L_plaster/(k_plaster*Area_plaster)
R_brick=L_brick/(k_brick*Area_brick)
R_2=1/(h_ext*Area_foam)

#here we calculate the parallel resistance made by plaster and brick
R_plast=2*(L_brick/(k_plaster*Area_plaster_lateral))
R_parallel=(R_brick*R_plast)/(R_brick+R_plast)
#done

R_tot=R_1+R_foam+(2*R_plaster)+R_parallel+R_2

Q_single=(T_in-T_out)/(R_tot)
Q_tot=tot_bricks*Q_single
print (Q_tot)
