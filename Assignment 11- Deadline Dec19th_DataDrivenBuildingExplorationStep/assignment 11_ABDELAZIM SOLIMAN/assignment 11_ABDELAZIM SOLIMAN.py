import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

DataFolderPath = "C:/Users/user/Desktop/_EETBS/Scientific_Python_Assignments_POLIMI_EETBS/Notebooks/Data"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 
DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0) 
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex
DF_consumption_dates = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_consumption_dates.head(5)
DF_consumption_dates.describe()

# Now let's import some weather data!
TemperatureFileName = "Austin_weather_2014.csv"
TemperatureFilePath = DataFolderPath+"/"+TemperatureFileName
DF_TemperatureSource = pd.read_csv(TemperatureFilePath,sep = ";",index_col=0)
previousIndex= DF_TemperatureSource.index
NewIndex = pd.to_datetime(previousIndex)
DF_TemperatureSource.index= NewIndex
series_temperature = DF_TemperatureSource['temperature']
DF_temperature = DF_TemperatureSource[['temperature']]
DF_temperaturedates = DF_temperature["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_temperaturedates.head(5)
DF_temperaturedates.describe()

# let's do the same for irradiation!!!
IrradianceFileName = "irradiance_2014_gen.csv"
IrradianceFilePath =  DataFolderPath+"/"+IrradianceFileName 
DF_irradiance = pd.read_csv(IrradianceFilePath, sep = ";",index_col= 1)
previousIndex1= DF_irradiance.index
NewIndex_irradianceSource = pd.to_datetime(previousIndex1)
DF_irradiance.index= NewIndex_irradianceSource
DF_irradiancedates = DF_irradiance["gen"]["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_irradiancedates[DF_irradiance["gen"] < 0] = 0
DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined.head(24)


fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(DF_consumption_dates.index.tolist(),DF_consumption_dates,'r')
ax1.set_ylabel('consumption',color='r')
ax2=ax1.twinx()
ax2.plot(DF_temperaturedates.index.tolist(),DF_temperaturedates,'b')
ax2.set_ylabel('temperature',color='b')
ax3=ax1.twinx()
ax3.plot(DF_irradiancedates.index.tolist(),DF_irradiancedates,'k')
ax3.set_ylabel('irradiance',color='k')