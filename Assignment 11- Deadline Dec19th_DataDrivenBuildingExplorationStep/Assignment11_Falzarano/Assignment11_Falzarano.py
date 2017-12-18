import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#recalling the file with consumption data from the folder
DataFolderPath = "C:/Users/Marica/Desktop/Data-driven_Building_simulation_Polimi_EETBS/Data"

#Import of data and then changing the index from string type to a data giving info about day and time
#consumption data
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 
DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0)     #reading the file

previousIndex = DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex

DF_June_1st_3rd_cons = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]


#weatherdata
weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = DataFolderPath+"/"+weatherSourceFileName
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep=";", index_col=0)

PreviousIndex_weatherSource = DF_weatherSource.index    
ParsedIndex_weatherSource = pd.to_datetime(PreviousIndex_weatherSource)
DF_weatherSource.index = ParsedIndex_weatherSource 


#irradiance data
IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath = DataFolderPath+"/"+IrradianceSourceFileName
DF_IrradianceSource = pd.read_csv(IrradianceSourceFilePath,sep=";",index_col=1)

PreviousIndex_IrradianceSource = DF_IrradianceSource.index    
ParsedIndex_IrradianceSource = pd.to_datetime(PreviousIndex_IrradianceSource)
DF_IrradianceSource.index = ParsedIndex_IrradianceSource



#I take the ambient temperature from the file with weather data and turn it into a data frame with only one column
#I restrain the data to the interval I want
series_temperature = DF_weatherSource['temperature']
DF_temperature = DF_weatherSource[['temperature']]


#I take the value of PV gen and put all the negative values to zero, because those values are meaningless
DF_irradiance = DF_IrradianceSource[["gen"]] 
DF_irradiance[DF_IrradianceSource["gen"] < 0] = 0


#I take the interval I need for the three sets of data
DF_June_1st_3rd_temp = DF_temperature["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_June_1st_3rd_irr = DF_irradiance["2014-06-01 00:00:00":"2014-06-03 23:00:00"]


#I put together the data of consumption, temperature and irradiance
DF_joined = DF_June_1st_3rd_cons.join([DF_June_1st_3rd_temp,DF_June_1st_3rd_irr])

#in this way I cancel all the NaN
DF_joined.dropna() 

#how to plot data with different magnitude order
fig, ax1 = plt.subplots()
ax1.plot(DF_June_1st_3rd_cons,"b")
ax1.set_xlabel('time')

# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('ac power', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(DF_June_1st_3rd_temp, 'r')
ax2.set_ylabel('temperature', color='r')
ax2.tick_params('y', colors='r')


ax3 = ax2.twinx()
ax3.plot(DF_June_1st_3rd_irr, 'g')
ax3.set_ylabel('irradiance', color='g')
ax3.tick_params('y', colors='g')

fig.tight_layout()
plt.show()

