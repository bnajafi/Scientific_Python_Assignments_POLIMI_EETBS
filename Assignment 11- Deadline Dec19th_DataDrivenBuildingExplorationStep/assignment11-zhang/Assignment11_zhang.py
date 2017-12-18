import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath="D:/Building System/Data-driven_Building_simulation_Polimi_EETBS/Data"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath= DataFolderPath+"/"+ConsumptionFileName
DF_consumption = pd.read_csv(ConsumptionFilePath,sep=",",index_col=0)
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex
DF_JunefirstTillthird = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_JunefirstTillthird.describe()

weatherFileName = "Austin_weather_2014.csv"
weatherFilePath = DataFolderPath+"/"+weatherFileName
DF_weather_source = pd.read_csv(weatherFilePath,sep = ";",index_col=0)
previousIndex= DF_weather_source.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_weather_source.index= NewparsedIndex
DF_temperature = DF_weather_source[["temperature"]]
DF_JunefirstTillthirdT = DF_temperature["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath = DataFolderPath+"/"+IrradianceSourceFileName
DF_irradiance_source = pd.read_csv(IrradianceSourceFilePath,sep = ";",index_col=1)
previousIndex= DF_irradiance_source.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_irradiance_source.index= NewparsedIndex
DF_irradiance = DF_irradiance_source[["gen"]]
DF_JunefirstTillthirdI = DF_irradiance["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
df_joined = DF_consumption.join([DF_temperature,DF_irradiance])
df_joined = df_joined.dropna()

df_chosen_dates = df_joined['2014-06-01':'2014-06-03']
df_chosen_dates.plot()

fig = plt.figure()
ax1 = fig.add_subplot(111) # axis for consumption
ax2 = ax1.twinx()          # axis for temperature
ax3 = ax1.twinx()  # axis for solar irradiance
rspine = ax3.spines['right']
rspine.set_position(('axes', 1.2))
consum_col='air conditioner_5545'


df_chosen_dates.plot(ax=ax1, y=consum_col, legend=False,color='b')
ax1.set_ylabel('Consumption',color='b')
ax1.tick_params(axis='y', colors='b')

df_chosen_dates.plot(ax=ax2, y='temperature', legend=False, color='g')
ax2.set_ylabel('Temperature deg C',color='g')
ax2.tick_params(axis='y',colors='g')

df_chosen_dates.plot(ax=ax3,y='gen',legend=False,color='r')
ax3.set_ylabel('Irradiance [from PV]',color='r')
ax3.tick_params(axis='y',colors='r')

ax1.set_xlabel('Time')
plt.show()
