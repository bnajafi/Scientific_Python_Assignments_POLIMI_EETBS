import os
os.chdir("D:/Polimi Piacenza/Energy and Environment/notes/3 Python Files and Guidelines/assignment10_khoudari")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

import fenestration_functions as func
import IntGains_Inf_Vent_DistrLosses as iv
import FunctionsOpaque as funcOp
import psySI as SI
import latent_functions as lat

#plotting two pie charts for heating and cooling in the basecase by extracting the final results from the updated data frame "results_wholeRFL_ibrahim.csv" 

results = pd.read_csv("results_wholeRFL_ibrahim.csv",sep=";",index_col=0)

results_heating_Piacenza = np.array([results["Heating"]["Q_opaque"],results["Heating"]["Q_windows"],results["Heating"]["Q_below"],
                           results["Heating"]["Q_internalGain"],results["Heating"]["Q_infiltVentilation"],results["Heating"]["Q_distribLosses"],
                           results["Heating"]["Q_latent"]])
labels_heat = ["opaque", "windows","Q_below","Q_internalGain", "infiltration/ventilation", "distributed losses","Q_latent"]

results_cooling_Piacenza = np.array([results["Cooling"]["Q_opaque"],results["Cooling"]["Q_windows"],results["Cooling"]["Q_below"],
                           results["Cooling"]["Q_internalGain"],results["Cooling"]["Q_infiltVentilation"],results["Cooling"]["Q_distribLosses"],
                           results["Cooling"]["Q_latent"]])
labels_cool = ["opaque", "windows","Q_below","Q_internalGain", "infiltration/ventilation", "distributed losses","Q_latent"]


plt.figure()
plt.pie(results_heating_Piacenza,explode=(0.01,0.01,0.01,0.01,0.01,0.01,0.01), labels = labels_heat, autopct = '%1.1f%%')
plt.title("HEATING LOADS PIACENZA")
plt.show()

plt.figure()
plt.pie(results_cooling_Piacenza,explode=(0.01,0.01,0.01,0.01,0.01,0.01,0.01), labels = labels_cool, autopct = '%1.1f%%')
plt.title("COOLING LOADS PIACENZA")
plt.show()

#bar graph for the variation of heating and cooling loads with different fenestration conditions

fenestration1 = pd.read_csv("results_wholeRFL__window_ibrahim1.csv",sep=";",index_col=0)
fenestration2 = pd.read_csv("results_wholeRFL_windows_ibrahim2.csv",sep=";",index_col=0)

tot_sens_heatings = [results["Heating"]["Q_sensible_tot"],fenestration1["Heating"]["Q_sensible_tot"],fenestration2["Heating"]["Q_sensible_tot"]]

tot_sens_coolings = [results["Cooling"]["Q_sensible_tot"],fenestration1["Cooling"]["Q_sensible_tot"],fenestration2["Cooling"]["Q_sensible_tot"]]

items = [1,2,3]
labels = ["basecase","reduced resistance","increased resistance"]
cols=["r","b","g"]

b1 = plt.bar(items,tot_sens_heatings,color="r",width=0.3)
b2 = plt.bar(items,tot_sens_coolings,color="b",width=0.3)
plt.title("Total Heating Load and cooling by Changing fenestration type")
plt.xticks(items,labels,color="g")
plt.xlabel("fenestration type")
plt.ylabel("Load,(W)")
plt.legend([b1,b2],["HeatingLoad","CoolingLoad"])



#bar graph for the variation of heating and cooling loads with different wall layers

wall1 = pd.read_csv("results_wholeRFL_walls_ibrahim1.csv",sep=";",index_col=0)
wall2 = pd.read_csv("results_wholeRFL_walls_ibrahim2.csv",sep=";",index_col=0)

tot_sens_heating = [results["Heating"]["Q_sensible_tot"],wall1["Heating"]["Q_sensible_tot"],wall2["Heating"]["Q_sensible_tot"]]

tot_sens_cooling = [results["Cooling"]["Q_sensible_tot"],wall1["Cooling"]["Q_sensible_tot"],wall2["Cooling"]["Q_sensible_tot"]]

b3 = plt.bar(items,tot_sens_heating,color="r",width=0.3)
b4 = plt.bar(items,tot_sens_cooling,color="b",width=0.3)
plt.title("Total Heating Load and cooling by Changing wall type")
plt.xticks(items,labels,color="g")
plt.xlabel("wall type")
plt.ylabel("Load,(W)")
plt.legend([b3,b4],["HeatingLoad","CoolingLoad"])

