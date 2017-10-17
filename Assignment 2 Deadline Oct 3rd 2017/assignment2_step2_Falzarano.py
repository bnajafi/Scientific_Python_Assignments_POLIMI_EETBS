# -*- coding: utf-8 -*-
#temperatures on the two sides of the wall
T_inf_1 = 20
T_inf_2 = -10

#IN SERIES

Rs1 = {"name": "foam", "area":0.25, "length": 0.03, "k": 0.026, "Res_value":0}        #foam layer
Rs2 = {"name": "plastic 1", "area":0.25, "length": 0.02, "k": 0.22, "Res_value":0}    #plastic layer 1
Rs3 = {"name": "plastic 2", "area":0.25, "length": 0.02, "k": 0.22, "Res_value":0}    #plastic layer 2

s = [Rs1, Rs2, Rs3]         

Rs_tot = 0

for i in s:
    i["Res_value"] = i["length"]/(i["area"]*i["k"])
    print ("The value of the resistance in " + i["name"] + " layer is " + str(i["Res_value"])+" °C/W")
    Rs_tot = Rs_tot + i["Res_value"]
    
print ("The total value of the conductive resistances in series is " + str(Rs_tot)+" °C/W")            #total conductive resistance in series
print (             )

#Convective resistance

R_conv_1 = {"name": "convective resistance 1", "area":0.25, "h": 10, "Res_value":0}
R_conv_2 = {"name": "convective resistance 2", "area":0.25, "h": 25, "Res_value":0}

c = [R_conv_1, R_conv_2]
Rc_tot = 0

for i in c:
    i["Res_value"] = 1/(i["area"]*i["h"])
    print ("The value of " + i["name"] + " is " + str(i["Res_value"])+" °C/W")
    Rc_tot = Rc_tot + i["Res_value"]
    
print ("The total value of the convective resistances is " + str(Rc_tot)+" °C/W")
print (             )

#IN PARALLEL
#Conductive resistances = [Area, Length, Conductivity]
Rp1 = {"name": "brick", "area":0.22,"length": 0.16, "k": 0.72, "Res_value":0}
Rp2 = {"name": "plastic layer 3", "area":0.015,"length": 0.16, "k": 0.22, "Res_value":0}
Rp3 = {"name": "plastic layer 4", "area":0.015,"length": 0.16, "k": 0.22, "Res_value":0}

p = [Rp1, Rp2, Rp3]
Rp_inv_tot = 0

for i in p:
    i["Res_value"] = i["length"]/(i["area"]*i["k"])
    print ("The value of the resistance in " + i["name"] + " is " + str(i["Res_value"])+" °C/W")
    Rp_inv = 1/i["Res_value"]
    Rp_inv_tot = Rp_inv_tot + Rp_inv

Rp_tot = 1/(Rp_inv_tot)
print ("The total value of the resistances in parallel is " + str(Rp_tot)+" °C/W")
print (             )

#total resistance list

R_tot = [Rs_tot, Rc_tot, Rp_tot]


#total heat loss

Q = (T_inf_1 - T_inf_2)/(sum(R_tot[0:]))

print ("The total thermal resistance of the unit is "+str(sum(R_tot[0:]))+" °C/W")

print ("The total heat loss through the unit is " + str(Q) + " W")


#whole wall data
Wall = {"area of a unit": 0.25,"height": 3, "width": 5}

Q_wall = Q*Wall["height"]*Wall["width"]/Wall["area of a unit"]


print ("The total heat loss through the wall is " + str(Q_wall) + " W")