H = 3 #height of the wall
W = 5 #width of the wall
ht = 0.25 #total height of the unit
hb = 0.22 #height of the brick
hp = 0.015 #height of the plaster
wf = 0.03 #width of the foam
wp = 0.02 #width of the plaster layers
wb = 0.16 #width of the brick
k1 = float (raw_input("enter the thermal conductivity of the foam in W/(degC*m) "))#foam conduction heat transfer
k2 = float (raw_input("enter the thermal conductivity of the plaster in W/(degC*m) ")) #plaster conduction heat transfer
k3 = float (raw_input("enter the thermal conductivity of the brick in W/(degC*m) ")) #brick conduction heat transfer
h1 = float (raw_input("enter the internal convenction heat transfer W/(degC*m^2) "))#inside convenction heat trasfer
h2 = float (raw_input("enter the external convenction heat tranfer W/(degC*m^2) "))#outside convenction heat trasfer
t1 = float (raw_input("enter the internal temperature in degC ")) #temperature inside
t2 = float (raw_input("enter the external temperature in degC ")) #temperature outside

#Resistence 
Rconv = 1/(h1*ht*1)
R1 = wf/(k1*ht*1) #foam Resistence
R2 = R6 = wp/(k2*ht*1) # the two plaster side resistence
R3 = R5 = wb/(k2*hp*1) # Plaster center Resistence
R4 = wb/(k3*hb*1) # Brick Resistence
R0 = 1/(h2*ht*1)  #second convention resistence

Rp = ( (1/R3) + (1/R4) + (1/R5) )
RP = 1/Rp #sum of the three resistence in the middle, they are in parallel

Rt = Rconv+R1+R2+RP+R6+R0

Q = (t1-(t2))/Rt #heat transfer through the wall
s = (ht*1) #surface area in m^2
Q1 = Q/s #heat transfer per m^2 area
A = H * W #total area

Qt = Q1*A


print"The amount of heat transfer of the entire wall is "+str (Qt)+" degC/W"
print"The amount of thermal resistence of the brick is "+str (Rt)+" W"