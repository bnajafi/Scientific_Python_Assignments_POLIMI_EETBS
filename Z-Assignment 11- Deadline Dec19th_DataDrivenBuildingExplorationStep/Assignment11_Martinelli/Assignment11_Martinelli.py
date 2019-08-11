# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "C:\Users\Utente\Desktop\Assignment11_Martinelli\Data"

ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 
DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0) 
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex
DF_JunefirstTillthird = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_JunefirstTillthird.describe()

plt.figure(1)
plt.plot(DF_JunefirstTillthird)
DF_JunefirstTillthird.plot()
plt.xlabel('Time')
plt.ylabel('AC Power [W]')
plt.show()

#first plot them separately, two alternative ways

WeatherSourceFileName = "Austin_weather_2014.csv"
WeatherSourceFilePath =  DataFolderPath+"/"+WeatherSourceFileName 
DF_weatherSource = pd.read_csv(WeatherSourceFilePath, sep = ";",index_col= 0)
DF_temperature = DF_weatherSource[['temperature']]
previousIndex_temperature= DF_temperature.index
NewparsedIndex_temperature = pd.to_datetime(previousIndex_temperature)
DF_temperature.index= NewparsedIndex_temperature
DF_JunefirstTillthirdTemp = DF_temperature["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

plt.figure(3)
plt.plot(DF_JunefirstTillthirdTemp)
DF_JunefirstTillthirdTemp.plot()
plt.xlabel('Time')
plt.ylabel('Ambient temperature[F]')
plt.show()

IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath =  DataFolderPath+"/"+IrradianceSourceFileName 
DF_irradianceSource = pd.read_csv(IrradianceSourceFilePath, sep = ";",index_col= 1)
DF_irradiance = DF_irradianceSource[["gen"]]
DF_irradiance[DF_irradianceSource["gen"] < 0] = 0
previousIndex_irradiance= DF_irradiance.index
NewparsedIndex_irradiance = pd.to_datetime(previousIndex_irradiance)
DF_irradiance.index= NewparsedIndex_irradiance
DF_JunefirstTillthirdIrr = DF_irradiance["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

plt.figure(5)
plt.plot(DF_JunefirstTillthirdIrr)
DF_JunefirstTillthirdIrr.plot()
plt.xlabel('Time')
plt.ylabel('Irradiance')
plt.show()

#then plot the on the same plot

DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_JunefirstTillthirdJoined = DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_joined.dropna()

plt.figure(7)
plt.plot(DF_JunefirstTillthirdJoined)
DF_JunefirstTillthirdJoined.plot()
plt.xlabel('Time')
plt.ylabel('AC Power [W],Ambient temperature,Irradiance')
plt.show()

#then plot them in the same plot with different scale for axis y

fig, ax1 = plt.subplots()

ax1.plot(DF_JunefirstTillthird, 'g')
ax1.set_xlabel('Time')
ax1.set_ylabel('AC Power', color='g')
ax1.tick_params('y', colors='g')

ax2 = ax1.twinx()
ax2.plot(DF_JunefirstTillthirdTemp, 'k')
ax2.set_ylabel('temp', color='k')
ax2.tick_params('y', colors='k')

ax3 = ax2.twinx()
ax3.plot(DF_JunefirstTillthirdIrr, 'c')
ax3.set_ylabel('Irr', color='c')
ax3.tick_params('y', colors='c')

fig.tight_layout()
plt.show()