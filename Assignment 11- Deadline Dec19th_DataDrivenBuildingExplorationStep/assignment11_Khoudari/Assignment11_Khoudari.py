
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "D:/Polimi Piacenza/Energy and Environment/notes/3 Python Files and Guidelines/assignment11_Khoudari"


#extracting consumption data
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 
DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0) 

previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex

#Extracting weather data
weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = DataFolderPath+"/"+weatherSourceFileName 
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep = ";",index_col=0)

# ## Visualizing the AC consumption with Temperature and Solar irradiance
# ### The temperature dataset is avaiable along with humidity, wind speed and more such paramters in a CSV format. For now we just take the temperature alone from the CSV file. Similarly we load the solar irradiance data.

previousIndex= DF_weatherSource.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_weatherSource.index= NewparsedIndex
DF_temperature = DF_weatherSource[["temperature"]]


#extracting irradiance data
IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath =  DataFolderPath+"/"+IrradianceSourceFileName 
DF_irradianceSource = pd.read_csv(IrradianceSourceFilePath, sep = ";",index_col= 1)

# The irradiance data was obtained from the PV generation units from the buildings. The system may sometimes record negative values, which makes no sense from an irradiance point of view. So the negative values have been set to zero after loading the data

previousIndex= DF_irradianceSource.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_irradianceSource.index= NewparsedIndex

DF_irradiance = DF_irradianceSource[["gen"]]

DF_irradiance[DF_irradianceSource["gen"] < 0] = 0   #giving a value of zero for each negative value


#joining them all together
DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])  #merging all the data together


DF_JunefirstTillthird = DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]    #choosing a specific date to work with

DF_JunefirstTillthird.dropna() #it will remove all Nans !!!

#plotting the variation of consumption,temperature and irradiance with respect to time
##plt.plot(DF_JunefirstTillthird["air conditioner_5545"])


fig = DF_JunefirstTillthird.plot()
plt.close()     
fig,ax1 = plt.subplots()   #creating an new empty plot
ax2 = ax1.twinx()   # ax1 and ax2 will have the same x-axis but different y-axis
ax3 = ax1.twinx()   # creating a new y-axis for ax3 on the same common x-axis of ax1 and ax2

rspine = ax3.spines['right']     #putting the y-axis of irradiance on the right
rspine.set_position(('axes', 1.07))    #the distance between irradiance and temperature y-axes
consum_col='air conditioner_5545'      #the original y-axis is for the consumption values

DF_JunefirstTillthird.plot(ax=ax1, y=consum_col, legend=False,color='b')
ax1.set_ylabel('Consumption',color='b')
ax1.tick_params(axis='y', colors='b')

DF_JunefirstTillthird.plot(ax=ax2, y='temperature', legend=False, color='g')
ax2.set_ylabel('Temperature deg C',color='g')
ax2.tick_params(axis='y',colors='g')

DF_JunefirstTillthird.plot(ax=ax3,y='gen',legend=False,color='r')
ax3.set_ylabel('Irradiance [from PV]',color='r')
ax3.tick_params(axis='y',colors='r')

ax1.set_xlabel('Time')
plt.show()
