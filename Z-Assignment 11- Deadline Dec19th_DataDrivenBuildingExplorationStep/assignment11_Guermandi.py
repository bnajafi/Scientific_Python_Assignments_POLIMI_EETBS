# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "/Users/federico/Desktop/roba/Data"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 

DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0) 
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex) #converts to datetime
DF_consumption.index= NewparsedIndex #update the index, now that is datetime
DF_consumption.head(24)
DF_JunefirstTillthird = DF_consumption["2014-06-01 00:00:00":"2014-06-04 00:00:00"] #creates the DataFrame we are going to use
DF_JunefirstTillthird.head(5)
DF_JunefirstTillthird.describe() #Data about the value of the previous DataFrame
# In[48]:



# Now let's import some weather data!
weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = DataFolderPath+"/"+weatherSourceFileName 
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep = ";",index_col=0)
DF_weatherSource.index

previousIndex_weatherSource= DF_weatherSource.index
NewparsedIndex_weatherSource = pd.to_datetime(previousIndex_weatherSource)
DF_weatherSource.index= NewparsedIndex_weatherSource

#  we usually do this
series_temperature = DF_weatherSource['temperature'] #series that contains temperature

# Nut now I would prefer to have it as a dataframe with just one column, we will then see why !!
DF_temperature = DF_weatherSource[['temperature']]

# let's do the same for irradiation!!!
IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath =  DataFolderPath+"/"+IrradianceSourceFileName 
DF_irradianceSource = pd.read_csv(IrradianceSourceFilePath, sep = ";",index_col= 1) #like in line 11
DF_irradianceSource.head(5)

previousIndex_irradianceSource= DF_irradianceSource.index
NewparsedIndex_irradianceSource = pd.to_datetime(previousIndex_irradianceSource)
DF_irradianceSource.index= NewparsedIndex_irradianceSource #Update the index 

# IF I want take just the column "gen " as a dataframe with a single column !
DF_irradiance = DF_irradianceSource[["gen"]] # to take it as a DF
DF_irradiance[DF_irradianceSource["gen"] < 0] = 0

DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined.head(24)

# what to do with Nans 
DF_joined.dropna() #it will remove all Nans !!!!! 

DF_tmepirr = DF_joined["2014-06-01 00:00:00":"2014-06-04 00:00:00"]


from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
#DF_JunefirstTillthird
#DF_tmepirr
index= DF_JunefirstTillthird.index
X = pd.to_datetime(index) #converts to datetime
 #update the index, now that is datetime

host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))

par2.axis["right"].toggle(all=True)


host.set_xlabel("Dates")
host.set_ylabel("AC [Watts]")
par1.set_ylabel("Temperature [C]")
par2.set_ylabel("Irradiance")

p1, = host.plot(X, DF_tmepirr["air conditioner_5545"] , label="AC [Watts]")
p2, = par1.plot(X, (DF_tmepirr["temperature"]-32)/1.8, label="Temperature")
p3, = par2.plot(X, DF_tmepirr["gen"], label="Irradiance")


host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())

plt.draw()
plt.show()