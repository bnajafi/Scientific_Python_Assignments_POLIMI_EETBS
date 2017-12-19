import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#I'm defining the path to read the tables
DataFolderPath = 'C:/Users/Utente/Dropbox/GIT/Data-driven_Building_simulation_Polimi_EETBS/Data'
ConsumptionFilename = 'consumption_5545.csv'
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFilename
#I'm reading the table and doing a data frame
DF_consumption= pd.read_csv(ConsumptionFilePath,sep=',',index_col=0)
previousindex=DF_consumption.index
ParsedIndex= pd.to_datetime(previousindex)
DF_consumption.index=ParsedIndex

DF_JunefirstTillthird = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]


#Now i plot the AC power and the Time
plt.figure('AC_Power-Time')
plt.plot(DF_JunefirstTillthird)
plt.xlabel('Time')
plt.ylabel('AC Power [W]')
plt.show()

#Importing weather data
weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = DataFolderPath+"/"+weatherSourceFileName 
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep = ";",index_col=0)
previousIndex_weatherSource= DF_weatherSource.index
NewparsedIndex_weatherSource = pd.to_datetime(previousIndex_weatherSource)
DF_weatherSource.index= NewparsedIndex_weatherSource

#The same of before but for temperature
DF_temperature = DF_weatherSource[['temperature']]
DF_JunefirstTillthird_temperature = DF_temperature["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

#Now i plot the Temperature and the time
plt.figure('Temperature-Time')
plt.plot(DF_JunefirstTillthird_temperature)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.show()
#The same for irradiance
IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath =  DataFolderPath+"/"+IrradianceSourceFileName 
DF_irradianceSource = pd.read_csv(IrradianceSourceFilePath,sep = ";",index_col= 1)

previousIndex_irradianceSource= DF_irradianceSource.index
NewparsedIndex_irradianceSource = pd.to_datetime(previousIndex_irradianceSource)
DF_irradianceSource.index= NewparsedIndex_irradianceSource

DF_irradiance = DF_irradianceSource[["gen"]]
DF_JunefirstTillthird_irradiance = DF_irradiance["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

#Now i plot the Temperature and the time
plt.figure('Irradiance-Time')
plt.plot(DF_JunefirstTillthird_irradiance)
plt.xlabel('Time')
plt.ylabel('Irradiance')
plt.show()

DF_joined = DF_consumption.join([DF_consumption,DF_temperature,DF_irradiance])
DF_JunefirstTillthird_joined = DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
#If i use this to plot i will have a scale problem. To avoid this i plot as follow

fig = plt.figure('Joined')
ax1 = fig.add_subplot(111)
ax1.plot(DF_JunefirstTillthird)
ax1.set_ylabel('Consumption',color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax2 = ax1.twinx()
ax2.plot(DF_JunefirstTillthird_temperature, 'r-')
ax2.set_ylabel('Temperature', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
    
ax3 = ax1.twinx()
ax3.plot(DF_JunefirstTillthird_irradiance, 'y-')
ax3.set_ylabel('Irradiance', color='y')
ax3.spines['right'].set_position(('outward', 50))
for tl2 in ax3.get_yticklabels():
    tl2.set_color('y')
plt.show()

