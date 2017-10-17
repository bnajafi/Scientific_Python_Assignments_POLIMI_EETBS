# -*- coding: utf-8 -*-
n = 0.0
m = 0.0
w = 0.0
j = 0.0
k = 0.0

#Temperatures
T_inf_1 = float(input ("Enter the temperature on the left side of the wall in °C "))
T_inf_2 = float(input ("Enter the temperature on the right side of the wall in °C "))


#layers in series
S = int(input("How many layers in series do you have? "))
A = float (input("Enter the value of the area in m2 "))

for n in range(1,S+1):
    
    ask = int(input ("Select the type of heat loss in the layer: write 1 for conductive; write 2 for convective "))
    if ask == 1:
            c = w
            L_s = float (input("Enter the length of layer " + str(n) + (" in m ")))
            k_s = float (input("Enter the value of the conductive heat transfer coefficient in W/m°C "))
                
            R_s = L_s/(k_s*A)
    
            print ("The value of resistance of layer " + str(n) + " is " + str(R_s) + " °C/W")
            w = c + R_s
    else:
            d = j
            h_s = float (input("Enter the value of the convective heat transfer coefficient of layer " + str(n) + (" in W/m°C ")))
                
            R_s = 1/(h_s*A)
    
            print ("The value of resistance of layer " + str(n) + " is " + str(R_s) + " °C/W")
            j = d + R_s
    
R_s_tot = w + j


#Layers in parallel
P = int(input("How many layers in parallel do you have? "))
L_p = float (input("Enter the length of the layers in m "))


for m in range(1,P+1):
    b = k
    k_p = float (input("Enter the conductive heat coefficient of layer " + str(m) + (" in m ")))
    A_p = float (input("Enter the value of the area in m2 "))
    
    R_p = L_p/(k_p*A_p)
    
    print ("The value of resistance of layer " + str(m) + " is " + str(R_p) + " °C/W")
    
    R_p_inv = 1/R_p
    
    k = b + R_p_inv
    
R_p_tot = 1/k


R_tot = R_p_tot + R_s_tot
print ("The total value of the resistance is " + str(R_tot))


Q = (T_inf_1 - T_inf_2)/R_tot
print ("The total heat loss through the unit is " + str(Q) + " W")


H = float(input("How big is your wall? Height in m "))
W = float (input("Width in m "))

A_wall = H*W

Q_wall = Q*A_wall/A

print ("The total heat loss through the wall is " + str(Q_wall) + " W")