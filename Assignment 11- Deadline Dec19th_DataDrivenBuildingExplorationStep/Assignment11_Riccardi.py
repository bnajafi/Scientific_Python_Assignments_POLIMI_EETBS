import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "C:\Users\Luca\Dropbox\git_fork\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 

DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0) 
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex

weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = DataFolderPath+"/"+weatherSourceFileName 
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep = ";",index_col=0)
DF_weatherSource.index

previousIndex_weatherSource= DF_weatherSource.index
NewparsedIndex_weatherSource = pd.to_datetime(previousIndex_weatherSource)
DF_weatherSource.index= NewparsedIndex_weatherSource

DF_temperature = DF_weatherSource[['temperature']]

IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath =  DataFolderPath+"/"+IrradianceSourceFileName 
DF_irradianceSource = pd.read_csv(IrradianceSourceFilePath, sep = ";",index_col= 1)

previousIndex_irradianceSource= DF_irradianceSource.index
NewparsedIndex_irradianceSource = pd.to_datetime(previousIndex_irradianceSource)
DF_irradianceSource.index= NewparsedIndex_irradianceSource

DF_irradiance = DF_irradianceSource[["gen"]]
DF_irradiance[DF_irradianceSource["gen"] < 0] = 0
DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined.dropna()
DF_JunefirstTillthird = DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

fig, ax1 = plt.subplots()
ax1.plot(DF_JunefirstTillthird.index,DF_JunefirstTillthird["air conditioner_5545"],'r')
ax1.set_xlabel("Time")
ax1.set_ylabel("Consumption [W]",color='r')
ax2=ax1.twinx()
ax2.plot(DF_JunefirstTillthird.index,DF_JunefirstTillthird["temperature"],'b')
ax2.set_ylabel("Temperature [F]",color='b')
ax3=ax1.twinx()
ax3.plot(DF_JunefirstTillthird.index,DF_JunefirstTillthird["gen"],'k')
ax3.set_ylabel("Irradiance [W/m^2]",color='k')
rspine = ax3.spines["right"]
rspine.set_position(("axes",1.07))


