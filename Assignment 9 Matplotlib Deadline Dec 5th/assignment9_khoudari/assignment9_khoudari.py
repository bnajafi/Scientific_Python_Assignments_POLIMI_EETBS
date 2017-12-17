import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Heating 

DT_Heating = 24.8

labels = ["wall","ceiling","door"]
cols=["b","r","y"]

Areas = [108,200,2.2]

Areas_series = pd.Series(Areas)

U_heating = [0.438,0.25,1.694]

U_heating_series = pd.Series(U_heating)

HF = DT_Heating*U_heating_series

HeatingLoadValues = HF*Areas_series

plt.close("all")
plt.figure()
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.title("Heating load Distribution")
plt.show()



#Cooling 

DT_Cooling = 7.9
DR_Cooling = 11.9
labels = ["wall","ceiling","door"]
cols=["g","b","r"]

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
A=OFt_series*DT_Cooling
B=OFr_series*DR_Cooling
C=A+B+OFb_series
CF = U_cooling_series*C
CoolingLoadValues = CF*Areas_series


plt.figure()
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.title("Cooling load Distrubtion")
plt.show()

#Modification of U

Modification = [0.7,1,1]

Mod_series = pd.Series(Modification)

U_heating_series_modified = U_heating_series*Mod_series

HF_modified = U_heating_series_modified*DT_Heating

HeatingLoadValues_modified = HF_modified*Areas_series

HeatingLoadTot = np.sum(HeatingLoadValues)

HeatingLoadModifiedTot = np.sum(HeatingLoadValues_modified)

HeatingLoads_Before_After = [HeatingLoadTot,HeatingLoadModifiedTot]

data = [1,2]
types = ["Unmodified U","Modified U"]

plt.figure()
plt.bar(data,HeatingLoads_Before_After,color="y")
plt.xticks(data,types,color="y")
plt.title("Variation of the Heating Load by the Effect of reducing U WALL by 30%")
plt.show()


