import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "C:\Users//alice\Desktop\Master PC\Buildings System\EETBS 2017-2018 POLIMI-PIACENZA\Assignments\Assignment11_Bortolotti\Data"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath + "/" + ConsumptionFileName
DF_consumption = pd.read_csv(ConsumptionFilePath, sep=",", index_col=0)
previousIndex = DF_consumption.index
ParseIndex = pd.to_datetime(previousIndex)
DF_consumption.index = ParseIndex

#Let's take a part of it!
#Since I'm interested in the period from June 1st until June 3rd 
DF_myChosenDates_comsumpion = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

DF_myChosenDates_comsumpion.plot() #way of plotting which is better optimization for pandas data frame
plt.xlabel("Time")
plt.ylabel("AC power (W)")

#Austin(weather data) 
weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = "C:\Users//alice\Desktop\Master PC\Buildings System\EETBS 2017-2018 POLIMI-PIACENZA\Assignments\Assignment11_Bortolotti\Data"
weatherSourceFilePath = DataFolderPath + "/" + weatherSourceFileName
DF_weatherSource = pd.read_csv(weatherSourceFilePath, sep=";", index_col=0) #to convert in DataFrame
previousIndex_weatherSource = DF_weatherSource.index
newParseIndex_weatherSource = pd.to_datetime(previousIndex_weatherSource)
DF_weatherSource.index = newParseIndex_weatherSource

DF_myChosenDates_temperature = DF_weatherSource["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_temperature = DF_myChosenDates_temperature[["temperature"]]

DF_temperature.plot()
plt.xlabel("Time")
plt.ylabel("Temperature(F)")

#Irradiance (gen=generation of PV)
irradianceSourceFileName = "irradiance_2014_gen.csv"
irradianceSourceFilePath = "C:\Users//alice\Desktop\Master PC\Buildings System\EETBS 2017-2018 POLIMI-PIACENZA\Assignments\Assignment11_Bortolotti\Data"
irradianceSourceFilePath = DataFolderPath + "/" + irradianceSourceFileName
DF_irradianceSource = pd.read_csv(irradianceSourceFilePath, sep=";",index_col=1)

previousIndex_irradianceSource = DF_irradianceSource.index
newParseIndex_IrradianceSource = pd.to_datetime(previousIndex_irradianceSource)
DF_irradianceSource.index = newParseIndex_IrradianceSource

DF_myChosenDates_irradiance = DF_irradianceSource["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_irradiance = DF_myChosenDates_irradiance[["gen"]] 
DF_irradiance[DF_myChosenDates_irradiance["gen"]<0]=0 #put equal to 0 the negative values

DF_irradiance.plot() #way of plotting which is better optimization for pandas data frame
plt.xlabel("Time")
plt.ylabel("Irradiance")

DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined_firstUntilThirdJune = DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_joined_firstUntilThirdJune.dropna() #it will remove all NaNs

DF_joined_firstUntilThirdJune.plot()
plt.xlabel("Time")
plt.ylabel("AC power(W),Temperature(F),Irradiance")

DF_joined_firstUntilThirdJune.dropna() #it will remove all NaNs

fig, ax1 = plt.subplots()

#make the y-axis label, ticks and tick labels match the line colour
ax1.plot(DF_myChosenDates_comsumpion,'g')
ax1.set_xlabel('Time')
ax1.set_ylabel('AC Power',color='g')
ax1.tick_params('y',colors='g')

ax2 = ax1.twinx()
ax2.plot(DF_temperature,'b')
ax2.set_ylabel('Temperature',color='b')
ax2.tick_params('y', colors='b')

ax3 = ax2.twinx()
ax3.plot(DF_irradiance,'r')
ax3.set_ylabel('Irradiance',color='r')
ax3.tick_params('y',colors='r')

fig.tight_layout()
plt.show()