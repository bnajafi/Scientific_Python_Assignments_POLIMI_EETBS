import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load the path of the Excel files for AC consumption, Weather and irradiance
DataPath="/Users/Marrugo/Dropbox/git_for_clone/Data-driven_Building_simulation_Polimi_EETBS/Data/"
consumption="consumption_5545.csv"
weather="Austin_weather_2014.csv"
irradiance="irradiance_2014_gen.csv"
#compiling the path for the Excel files of AC consumption, Weather and irradiance
ConsumpitionFile=DataPath+consumption
Weather=DataPath+weather
Irradiance=DataPath+irradiance
#import data frame of the values for AC consuption, Weather and irradiance
DF_consumption=pd.read_csv(ConsumpitionFile,sep=",",index_col=0)
DF_weather=pd.read_csv(Weather,sep=";",index_col=0)
DF_irradiance=pd.read_csv(Irradiance,sep=";",index_col=1)
#Change the index of the Data frame of weather to data time 
previusindex=DF_weather.index
parsedindex=pd.to_datetime(previusindex)
DF_weather.index=parsedindex
#Change the index of the Data frame of irradiance to data time
previusindex=DF_irradiance.index
parsedindex=pd.to_datetime(previusindex)
DF_irradiance.index=parsedindex
#Change the index of the Data frame of consumption to data time
previusindex=DF_consumption.index
parsedindex=pd.to_datetime(previusindex)
DF_consumption.index=parsedindex
DF_consumption.head()
#Selecting the rage of AC consuption, Weather and irradiance between June 1th of 2014 until June 3th of 2014
RangeDateConsumption=DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
RangeDateWeather=DF_weather[["temperature"]]["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
RangeDateIrradiance=DF_irradiance[["gen"]]["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
#Correcting Irradiance data
RangeDateIrradiance[RangeDateIrradiance["gen"]<0]=0
#Compiling data of AC consuption, Weather and irradiance
DF_DataTexas=RangeDateConsumption.join([RangeDateWeather,RangeDateIrradiance])
#Ploting the data
DF_DataTexas.plot()
plt.xlabel("time")
plt.ylabel("AC consumption (W)")

#Ploting using subplots a double Y axis

#Defining number of subplots
f, axes = plt.subplots(2, 1)
#Ploting in subplot 1 data of AC consumption
axes[0].plot(RangeDateConsumption, 'b-')
#Y label for AC consumption in subplot 1
axes[0].set_ylabel('AC consumption (W)', color='b')
axes[0].tick_params('y', colors='b')
#Creating double Y axis in subplot 1
ax21 = axes[0].twinx()
#Ploting in subplot 1 data of weather
ax21.plot(RangeDateWeather, 'r-')
#Y label weather in subplot 1
ax21.set_ylabel('Temperature (F)', color='r')
ax21.tick_params('y', colors='r')
#Ploting in subplot 2 data of AC consumption
axes[1].plot(RangeDateConsumption, 'b-')
#x label for all data in all subplots 
axes[1].set_xlabel('Time (Data time)')
#Y label for AC consumption in subplot 1
axes[1].set_ylabel('AC consumption (W)', color='b')
axes[1].tick_params('y', colors='b')
#Creating double Y axis in subplot 2
ax22 = axes[1].twinx()
#Ploting in subplot 2 data of Irradiance
ax22.plot(RangeDateIrradiance, 'r-')
#Y label for Irradiance in subplot 2
ax22.set_ylabel('Irradiance (W/m2)', color='r')
ax22.tick_params('y', colors='r')
plt.show()