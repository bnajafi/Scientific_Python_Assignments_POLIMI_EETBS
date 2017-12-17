
import pandas as pd
import matplotlib.pyplot as plt

labels=["walls","ceiling","door"]
cols=["purple","g","b"]

#----Q-vlues from example--------#

Qheating=[1149.2,1240,92.5]
Qcooling=[547.2,514.6,43]

#----Pie-charts for Both loads----#

plt.pie(Qcooling, labels = labels, colors = cols, startangle=90, explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.title("Qcooling of opaque surfaces")

Figure=plt.figure()
plt.pie(Qheating, labels = labels, colors = cols, startangle=90, explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.title("Qheating of opaque surfaces")


#----Heating load of the opaque surfaces in function of the U value of the external wall

def Qopaque_heating_calculation (Qheating_series):
    Qopaque_heating = Qheating_series + Qheating[1] + Qheating [2]   #Here 1 is for ceiling & 2 is for doors
    return Qopaque_heating

Area = 105.8        #square meters
deltaT = 24.8       #Temp; difference
U_series = pd.Series(range(0,100,10))      #0 to 100 aibitary values are taken with difference of 10

Qheating_serie = U_series * Area * deltaT
Qopaque_heating = Qheating_serie.apply(Qopaque_heating_calculation)

#---2D Plot of above function----#

figure2 = plt.figure()
plt.scatter(U_series,Qopaque_heating, label="U value of external wall", color="black", marker="*",s=100)
plt.xlabel("U value of external wall")
plt.ylabel("Overall opaque heating load")
plt.title("Effect of U-Value(External wall) on Opaque Heating Load")