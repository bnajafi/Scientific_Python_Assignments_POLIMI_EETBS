import os
os.chdir("C:\Users\Marica\Desktop\python assignments")


from wallCalculations_Falzarano import wallCalculations

layer_ser=["inside","woodbevel","woodfiber","gypsum","outside"]
layer_par=["glassfiber","stud"]
frac_area = 0.75

walldt = wallCalculations(layer_ser,layer_par,frac_area)
U = walldt["U_overall"]



from wallCalculations_Falzarano import a
listdoor = ["outside", "inside", "wood"]
a(listdoor)

doordata = a(listdoor)
U_door = doordata["Total U"]


listceiling = ["outside","inside","glassfiber", "gypsum", "wood"]
ceilingdata = a(listceiling)

U_ceiling = ceilingdata["Total U"]

delta_T = 24.8
A_ceil = 200
A_door = 2.2
A_wall = 105.8

Q_wall = U*delta_T*A_wall
Q_door = U_door*delta_T*A_door
Q_ceil = U_ceiling*delta_T*A_ceil

Q_tot = Q_wall + Q_door + Q_ceil
