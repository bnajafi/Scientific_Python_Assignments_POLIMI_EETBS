import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "C:\Users\Giulia\Desktop\Buildings\python\Assignment\Assignment11_Botti"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 

DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0) 
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex
DF_JunefirstTillthird = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_JunefirstTillthird.describe()

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

DF_irradiance = DF_irradianceSource[["gen"]] # to take it as a DF
DF_irradiance[DF_irradianceSource["gen"] < 0] = 0
DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined.dropna()
DF_joined_3Days = DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

plt.figure()
DF_joined_3Days.plot()
plt.xlabel('Time')
plt.ylabel('AC Power [W]')
plt.show()