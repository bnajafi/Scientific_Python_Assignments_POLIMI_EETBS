import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Heating pie chart

DT_winter = 24.8

labels = ["wall","ceyling","door"]
cols=["r","b","g"]

Areas = [108,200,2.2]

Areas_series = pd.Series(Areas)

U_heating = [0.438,0.25,1.694]

U_heating_series = pd.Series(U_heating)

HF = DT_winter*U_heating_series

HeatingLoadValues = HF*Areas_series

plt.close("all")
plt.figure()
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.title("Heating load partition")
plt.show()



#Cooling pie chart

DT_summer = 7.9
DR_summer = 11.9
labels = ["wall","ceyling","door"]
cols=["r","b","g"]

Areas = [108,200,2.2]

Areas_series = pd.Series(Areas)

U_cooling = [0.435,0.25,1.655]

U_cooling_series = pd.Series(U_cooling)

OFt = [1,0.62,1]
OFt_series = pd.Series(OFt)
OFb = [8.2,7.655,8.2]
OFb_series = pd.Series(OFb)
OFr = [-0.36,-0.19,-0.36]
OFr_series = pd.Series(OFr)
A=OFt_series*DT_summer
B=OFr_series*DR_summer
C=A+B+OFb_series
CF = U_cooling_series*C
CoolingLoadValues = CF*Areas_series


plt.figure()
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.title("Cooling load partition")
plt.show()

#Modification of U

Modification = [0.8,1,1]

Modification_series = pd.Series(Modification)

U_heating_series_modified = U_heating_series*Modification_series

HF_modified = U_heating_series_modified*DT_winter

HeatingLoadValues_modified = HF_modified*Areas_series

HeatingLoadTot = np.sum(HeatingLoadValues)

HeatingLoadModifiedTot = np.sum(HeatingLoadValues_modified)

HeatingLoads_Before_After = [HeatingLoadTot,HeatingLoadModifiedTot]

items = [1,2]
types = ["Unmodified U","Modified U"]

plt.figure()
plt.bar(items,HeatingLoads_Before_After,color="b")
plt.xticks(items,types,color="b")
plt.title("Variation of Heating Load reducing U WALL by 20%")
plt.show()


