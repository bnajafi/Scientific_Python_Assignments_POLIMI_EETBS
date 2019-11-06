
wall_height = 3
wall_width = 5
wall_area = 0.25

inside_temperature = 20
outside_temperature = -10 

inside_h = 10
outside_h = 25

foam_width = 0.03
foam_k = 0.026
foam_area = 0.25

plaster_side_layer_area = 0.25
plaster_side_layer_width = 0.02
plaster_side_layer_k = 0.22

plaster_center_layer_area = 0.015
plaster_center_layer_width = 0.16
plaster_center_layer_k = 0.22

brick_area = 0.22
brick_width = 0.16
brick_k = 0.72 

#Resistence calculation: 
R_inside_conv = 1/(inside_h*wall_area)
R_outside_conv = 1/(outside_h*wall_area)
foam_R = foam_width/(foam_k*foam_area)
plaster_side_layer_R_1 = plaster_side_layer_width/(plaster_side_layer_k*plaster_side_layer_area)
plaster_side_layer_R_2 = plaster_side_layer_R_1
plaster_center_layer_R_1 = plaster_center_layer_width/(plaster_center_layer_k*plaster_center_layer_area) 
plaster_center_layer_R_2 = plaster_center_layer_R_1
brick_R = brick_width/(brick_k*brick_area)

R_parallel = 1/((1/brick_R)+(1/plaster_center_layer_R_1)+(1/plaster_center_layer_R_2))

R_tot = R_inside_conv+foam_R+plaster_side_layer_R_1+plaster_side_layer_R_2+R_parallel+R_outside_conv

Q_unit=(inside_temperature-outside_temperature)/R_tot
Q_wall=Q_unit*wall_height*wall_width/wall_area

print"R value: "+str (R_tot)
print"Q value: "+str (Q_wall)