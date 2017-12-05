# -*- coding: utf-8 -*-
unit_height = float(raw_input("unit height: "))
unit_width = float(raw_input("unit width")) 

inside_h = float(raw_input("inside heat transfer coefficient: "))
R_inside_conv = 1/(unit_width*unit_height*inside_h)

foam_k = float(raw_input("foam heat transfer coefficient: "))
foam_width = float(raw_input("foam thickness: "))
foam_R = foam_width/(unit_width*unit_height*foam_k)

plaster_side_layer_k = float(raw_input("plastic side layer heat transfer coefficient: "))
plaster_side_layer_width = float(raw_input("plastic layer thickness: "))
plaster_side_layer_R_1 = plaster_side_layer_width/(unit_width*unit_height*plaster_side_layer_k)
plaster_side_layer_R_2 = plaster_side_layer_R_1

plaster_center_layer_k = float(raw_input("plastic center layer heat transfer coefficient: "))
plaster_center_layer_width = float(raw_input("plastic center layer thickness: "))
plaster_center_layer_height = float(raw_input("plastic center layer height: "))
plaster_center_layer_R_1 = plaster_center_layer_width/(plaster_center_layer_height*unit_width*plaster_center_layer_k)
plaster_center_layer_R_2 = plaster_center_layer_R_1

brick_k = float(raw_input("brick heat transfer coefficient: "))
brick_width = float(raw_input("brick thickness: "))
brick_height = float(raw_input("brick height: "))
brick_R = brick_width/(brick_height*unit_width*brick_k) 

outside_h = float(raw_input("outisde heat transfer coefficient: "))
R_outside_conv = 1/(unit_width*unit_height*outside_h)

R_parallel = 1/((1/brick_R)+(1/plaster_center_layer_R_1)+(1/plaster_center_layer_R_2))

R_tot = R_inside_conv+foam_R+plaster_side_layer_R_1+plaster_side_layer_R_2+R_parallel+R_outside_conv

inside_temperature = float(raw_input("inside temperature: "))
outside_temperature=float(raw_input("outside temperature: "))
Q_unit=(inside_temperature-outside_temperature)/R_tot

wall_width =float(raw_input("wall width: "))
wall_height = float(raw_input("wall height: ")) 

Q_wall=Q_unit*wall_height*wall_width/(unit_width*unit_height)

print"R value: "+str (R_tot)
print"Q value: "+str (Q_wall)