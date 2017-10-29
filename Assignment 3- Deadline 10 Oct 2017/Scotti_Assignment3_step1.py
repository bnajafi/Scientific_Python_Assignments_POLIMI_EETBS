#Assignment 3

#Dictionary of resistances
Material={"out_winter":0.03, "out_summer":0.044, "int":0.12, "cement":0.018, "plywood":0.11, "paper":0.011, "tile": 0.32, "stud_140":0.98, "stud_90":0.63, "fiber_90":2.45, "fiber_25":0.7, "fiberboard":0.23, "bevel": 0.14, "wallboard":0.079}

Layers_serie = ["bevel", "fiberboard", "wallboard"]
Layers_parallel = ["fiber_90", "stud_90"]

ratio=0.75

#Total unit thermal resistance as value and list
R_serie=0
for anylayer in Layers_serie:
    R_serie=R_serie+Material[anylayer] 

R_tot=[]
for anylayer in Layers_parallel:
    R_value = Material[anylayer]+R_serie
    R_tot.append(R_value)

#tot U
U_tot = ratio * R_tot[0]**-1+(1-ratio)*R_tot[1]**-1

#now we make calculation for real wall
p = 0.2
P = 50
h=2.5
T_in = 22
T_out = -2
Q_tot = (1-p)*P*h*U_tot*(T_in-T_out)
print ("the heat loss along the wall is ") + str(Q_tot)