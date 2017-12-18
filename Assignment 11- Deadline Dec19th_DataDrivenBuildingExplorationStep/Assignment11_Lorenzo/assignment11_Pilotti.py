# Assignment 11


import pandas as pd
import matplotlib.pyplot as plt


DataFolderPath="C:/Users/Lorenzo/Dropbox_Polimi_PC/Dropbox/git_fork/Data-driven_Building_simulation_Polimi_EETBS/Data"
ConsumptionSourceName="consumption_5545.csv"
ConsumptionSourcePath=DataFolderPath + "/" + ConsumptionSourceName
DF_consumption=pd.read_csv(ConsumptionSourcePath, sep=",", index_col=0)
# converting the indexes
ParseIndex=pd.to_datetime(DF_consumption.index)
# dataframe with the indexes updated
DF_consumption.index=ParseIndex

# to extratc the consumptions over a period of time
DF_TimePeriod_consumption=DF_consumption["2014-06-01 00:00:00" : "2014-06-03 23:00:00"]


# importing the weather data
weatherSourceFileName="Austin_weather_2014.csv"
weatherSourceFilePath=ConsumptionFilePath=DataFolderPath + "/" + weatherSourceFileName
DF_weatherSource=pd.read_csv(weatherSourceFilePath, sep=";", index_col=0)
NewParsedIndex_weatherSource=pd.to_datetime(DF_weatherSource.index)
DF_weatherSource.index=NewParsedIndex_weatherSource

# dataframe of one colum for temperature 
DF_temperature=DF_weatherSource[["temperature"]]
DF_temperature=(DF_temperature["temperature"]-32)/1.8
DF_temperature_TimePeriod=DF_temperature["2014-06-01 00:00:00" : "2014-06-03 23:00:00"]

# the same for irradiation
IrradianceSourceFileName="irradiance_2014_gen.csv"
IrradianceSourcePath=ConsumptionFilePath=DataFolderPath + "/" +IrradianceSourceFileName
DF_irradianceSource=pd.read_csv(IrradianceSourcePath, sep=";", index_col=1)

# dataframe with a single column
DF_irradiance=DF_irradianceSource[["gen"]]
# taking only positive values
DF_irradiance[DF_irradiance["gen"]<0]=0
# updating the indexes as date
NewParsedIndex_irradianceSource=pd.to_datetime(DF_irradiance.index)
DF_irradiance.index=NewParsedIndex_irradianceSource
DF_irradiance_TimePeriod=DF_irradiance["2014-06-01 00:00:00" : "2014-06-03 23:00:00"]

# plot AC consumptions, temperature and irradiation in the same graph

DF_joined_Consump_Temp_Irr=DF_TimePeriod_consumption.join([DF_temperature_TimePeriod, DF_irradiance_TimePeriod])
DF_joined_cleaned=DF_joined_Consump_Temp_Irr.dropna()   #Data Cleaning
DF_joined_cleaned.plot()

# since the scale of the plotted value for temperature and irradiace is different than of AC consumption:
fig=plt.figure()
ax1 = fig.add_subplot(111) # axis for consumption
ax2 = ax1.twinx()          # axis for temperature
ax3 = ax1.twinx()          # axis for solar irradiance
rspine = ax3.spines['right']
rspine.set_position(('axes', 1.05))

DF_joined_cleaned.plot(ax=ax1, y="air conditioner_5545", legend=True,color='b')
ax1.set_ylabel('AC Consumption [W]',color='b')
ax1.tick_params(axis='y', colors='b')


DF_joined_cleaned.plot(ax=ax2, y='temperature', legend=False, color='r')
ax2.set_ylabel('Temperature [C]',color='r')
ax2.tick_params(axis='y',colors='r')

DF_joined_cleaned.plot(ax=ax3,y='gen',legend=False,color='y')
ax3.set_ylabel('Irradiance [W/m2]',color='y')
ax3.tick_params(axis='y',colors='y')
ax1.set_xlabel('Time')

plt.title("Correlation between AC consumption, temperature and irradiation")