#Assignment 11 - Depalo

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "C:/Users/MonicaDepp/Dropbox/GitBash/gitForkClone/Data-driven_Building_simulation_Polimi_EETBS/Data"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 
AmbientFileName = "Austin_weather_2014.csv"
AmbientFilePath = DataFolderPath+"/"+AmbientFileName
IrradianceFileName = "irradiance_2014_gen.csv"
IrradianceFilePath = DataFolderPath+"/"+IrradianceFileName

#importing the excel files as pandas dataframes:
DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0) 
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex

DF_ambient = pd.read_csv(AmbientFilePath,sep = ";",index_col=0) 
previousIndex2= DF_ambient.index
NewparsedIndex2 = pd.to_datetime(previousIndex2)
DF_ambient.index= NewparsedIndex2
DF_temperature = DF_ambient[['temperature']]      #extracting only the column "temperature"

DF_irradiance = pd.read_csv(IrradianceFilePath,sep = ";",index_col=1) 
previousIndex3= DF_irradiance.index
NewparsedIndex3 = pd.to_datetime(previousIndex3)
DF_irradiance.index= NewparsedIndex3
DF_irrGen = DF_irradiance[["gen"]]             #extracting only the column "gen" for PV generation
DF_irrGen[DF_irradiance["gen"] < 0] = 0        #making all slightly negative values become zero

#extracting data from 1st June to 3rd June 2014:
DF_JunefirstTillthirdCons = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_JunefirstTillthirdCons.describe()
DF_JunefirstTillthirdGen = DF_irrGen["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_JunefirstTillthirdGen.describe()
DF_JunefirstTillthirdTemp = DF_temperature["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_JunefirstTillthirdTemp.describe()

#creating the plot:
fig = plt.figure('Consumption vs. PV Gen. vs. Temp')
ax1 = fig.add_subplot(111)
ax1.plot(DF_JunefirstTillthirdCons, 'skyblue')       #adding first consumption data
ax1.set_ylabel('AC Comsumption', color='skyblue')
ax1.set_xlabel('Time')
for tl in ax1.get_yticklabels():                    #changing color of the y values labels
    tl.set_color('skyblue')
ax2 = ax1.twinx()                                   #creating a second y axis for PV generation
ax2.plot(DF_JunefirstTillthirdGen, 'slateblue')
ax2.set_ylabel('PV Generation', color='slateblue')
for tl in ax2.get_yticklabels():
    tl.set_color('slateblue')
ax3 = ax1.twinx()
ax3.plot(DF_JunefirstTillthirdTemp, 'lightseagreen')
ax3.set_ylabel('Temperature', color='lightseagreen')
ax3.spines['right'].set_position(('outward',60))     #third y axis to the right, 60 pixels distant from the other
for tl in ax3.get_yticklabels():
    tl.set_color('lightseagreen')
plt.title('Temp, PV gen and consumption from 1st June to 3rd June 2014')
plt.tight_layout()
plt.show()