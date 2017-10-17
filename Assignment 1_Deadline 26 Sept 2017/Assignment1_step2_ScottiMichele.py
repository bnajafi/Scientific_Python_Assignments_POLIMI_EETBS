#EXERCISE 1, step 2

h_tot = float(raw_input('Insert the total height of the wall '))
h_brick = float(raw_input('Insert the total height of the single brick '))
h_plaster = float(raw_input('Insert the total height of the single plaster '))

width_tot = float(raw_input('Insert the total width of the wall '))
width_block = float(raw_input('Insert the total width of the single module '))

L_foam = float(raw_input('Insert the lenght of the foam '))
L_plaster = float(raw_input('Insert the lenght of the plaster '))
L_brick = float(raw_input('Insert the lenght of the brick '))

Area_tot=h_tot*width_tot
Area_foam=width_block*((2*h_plaster)+h_brick)
Area_plaster=Area_foam
Area_plaster_lateral=h_plaster*width_block
Area_brick=width_block*h_brick
tot_bricks=Area_tot/(Area_foam)

T_in = float(raw_input('Insert the temperature into the edifice '))
T_out = float(raw_input('Insert the temperature outside the edifice '))

h_int = float(raw_input('Insert the value of h_int '))
h_out = float(raw_input('Insert the value of h_out '))

k_foam = float(raw_input('Insert the value of k_foam '))
k_brick = float(raw_input('Insert the value of k_brick '))
k_plaster = float(raw_input('Insert the value of k_plaster '))

#CALCULATIONS
#Here there are the simpliest resistances
R_1=1/(h_int*Area_foam)
R_foam=L_foam/(k_foam*Area_foam)
R_plaster=L_plaster/(k_plaster*Area_plaster)
R_brick=L_brick/(k_brick*Area_brick)
R_2=1/(h_out*Area_foam)

#here we calculate the parallel resistance made by plaster and brick
R_plast=2*(L_brick/(k_plaster*Area_plaster_lateral))
R_parallel=(R_brick*R_plast)/(R_brick+R_plast)
#done

R_tot=R_1+R_foam+(2*R_plaster)+R_parallel+R_2

Q_single=(T_in-T_out)/(R_tot)
Q_tot=tot_bricks*Q_single

print (Q_tot)