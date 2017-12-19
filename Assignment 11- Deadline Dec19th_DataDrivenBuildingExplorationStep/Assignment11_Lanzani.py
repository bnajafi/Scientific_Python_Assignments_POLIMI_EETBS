import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns


DataFolderPath="C:\Users\marco\Desktop\GIT\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath= DataFolderPath+"/"+ConsumptionFileName
DF_consumption = pd.read_csv(ConsumptionFilePath,sep=",",index_col=0)
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex
DF_JunefirstTillthird = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

weatherFileName = "Austin_weather_2014.csv"
weatherFilePath = DataFolderPath+"/"+weatherFileName
DF_weather_source = pd.read_csv(weatherFilePath,sep = ";",index_col=0)
previousIndex= DF_weather_source.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_weather_source.index= NewparsedIndex
DF_temperature = DF_weather_source[["temperature"]]
DF_temperature_FirstThird=DF_temperature["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath = DataFolderPath+"/"+IrradianceSourceFileName
DF_irradiance_source = pd.read_csv(IrradianceSourceFilePath,sep = ";",index_col=1)
previousIndex= DF_irradiance_source.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_irradiance_source.index= NewparsedIndex
DF_irradiance = DF_irradiance_source[["gen"]]
DF_irradiance[DF_irradiance_source["gen"] < 0] = 0
DF_irradiance_FirstThird=DF_irradiance["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

DF_joined = DF_JunefirstTillthird.join([DF_temperature_FirstThird,DF_irradiance_FirstThird])


DF_joined.plot()
#DF_joined.set_ylabel('temperature',color='b')
plt.xlabel('Time')
plt.show()