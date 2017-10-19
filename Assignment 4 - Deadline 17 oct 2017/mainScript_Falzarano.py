import os
os.chdir("C:\\Users\Marica\Desktop\python assignments")


from wallCalculations_Falzarano import wallCalculations

layer_ser=["inside","woodbevel","woodfiber","gypsum","outside"]
layer_par=["glassfiber","stud"]
frac_area = 0.75

walldt = wallCalculations(layer_ser,layer_par,frac_area)
U = walldt["U_overall"]
print("the overall value of U is " + str(U))


from wallCalculations_Falzarano import wallCalc_series
listK = ["outside", "inside", "woodbevel", "woodfiber", "gypsum"]
wallCalc_series(listK)