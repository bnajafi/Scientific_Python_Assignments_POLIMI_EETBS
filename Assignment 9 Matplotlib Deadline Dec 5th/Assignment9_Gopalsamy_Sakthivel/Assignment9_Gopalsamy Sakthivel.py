import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

labels = ["wall","door","ceiling"]
cols=["r","b","g"]

###########Heating load calculations#############
Areas = [105.8,2.2,200]
Areas_series = pd.Series(Areas)
U_heating = [0.438,1.695,0.25]
U_heating_series = pd.Series(U_heating)
DT_heating = 24.8
HeatingLoadsOpaque=Areas_series*U_heating_series*DT_heating
###########Plotting Heating loads#############
plt.close("all")
plt.figure()
plt.pie(HeatingLoadsOpaque,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.title("Heating load partition")
plt.show()

###########Cooling load calculations#############
DT_cooling = 7.9
DR = 11.9
OFt = [1,1,0.62]
OFt_series = pd.Series(OFt)
OFb=[8.2,8.2,7.655]
OFb_series=pd.Series(OFb)
OFr=[-0.36,-0.36,-0.19]
OFr_series=pd.Series(OFr)
CoolingLoadsOpaque=Areas_series*U_heating_series*((OFt_series*DT_cooling)+OFb_series+(OFr_series*DR))
###########Plotting Cooling loads#############
plt.figure()
plt.pie(CoolingLoadsOpaque,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.title("Cooling load partition")
plt.show()


########### "U - Modification" #############
Modification = [0.62,1,1]
Modification_series = pd.Series(Modification)
U_heating_series_modified = U_heating_series*Modification_series
HeatingLoadsOpaqueModified=Areas_series*U_heating_series_modified*DT_heating

HeatingLoadTot = np.sum(HeatingLoadsOpaque)
HeatingLoadModifiedTot = np.sum(HeatingLoadsOpaqueModified)

HeatingLoads_Before_After = [HeatingLoadTot,HeatingLoadModifiedTot]

items = [1,2]
types = ["Unmodified U","Modified U"]

plt.figure()
plt.bar(items,HeatingLoads_Before_After,color="cyan")
plt.xticks(items,types,color="r")
plt.title("Variation of Heating Load reducing U Wall by 38%")
plt.show()