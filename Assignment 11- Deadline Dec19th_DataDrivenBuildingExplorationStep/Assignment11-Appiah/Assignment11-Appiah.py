import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DataFolderPath = "C:/Users/Akwesi/Documents/GIT/Data-driven_Building_simulation_Polimi_EETBS/Data" #for the data directory

# For the Consumption file
ConsumptionFileName = "consumption_5545.csv" #The CSV data file
ConsumptionFilePath= DataFolderPath+"/"+ConsumptionFileName  #to call the folder path containing the csv file
DF_consumption = pd.read_csv(ConsumptionFilePath,sep=",",index_col=0) 
previousIndex = DF_consumption.index  # to take the index
NewparsedIndex = pd.to_datetime(previousIndex) #to_datatime convert the date index to real date
DF_consumption.index= NewparsedIndex # to assign the new index with the old index

# For the weather file
weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = DataFolderPath+"/"+weatherSourceFileName
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep=";",index_col =0)
previousIndex_weatherSource = DF_weatherSource.index
NewparsedIndex_weatherSource =  pd.to_datetime(previousIndex_weatherSource)
DF_weatherSource.index = NewparsedIndex_weatherSource
DF_Temperature = DF_weatherSource[["temperature"]]  #the get it in data frame

#For irradiation
irradiatianceSourceFileName = "irradiance_2014_gen.csv"
irradiatianceSourceFilePath = DataFolderPath+"/"+irradiatianceSourceFileName
DF_irradiatianceSource = pd.read_csv(irradiatianceSourceFilePath,sep=";",index_col =1)
DF_irradiatianceSource.head(5)
previousIndex_irradiatianceSource = DF_irradiatianceSource.index
NewparsedIndex_irradiatianceSource =  pd.to_datetime(previousIndex_irradiatianceSource)
DF_irradiatianceSource.index = NewparsedIndex_irradiatianceSource

#to take the column gen which is the Pv generation to represent irradiance
DF_irradiance = DF_irradiatianceSource[["gen"]]  #the get it in data frame
DF_irradiance[DF_irradiatianceSource[["gen"]] <0] = 0  #makes all the negative values zero..i.e cleaning up the data


#to put all together in a Data frame...concumption, Temperature and Irradiance...we use .join function
DF_joined =  DF_consumption.join([DF_Temperature,DF_irradiance])

#To see the data for the defined time period 10th-12th June
DF_mychosenDates =DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"] 
DF_mychosenDates.dropna() # to remove all the NaNs.

#plotting the variation of consumption,temperature and irradiance with respect to time
fig = DF_mychosenDates.plot()
plt.close()     
fig,ax1 = plt.subplots()   
ax2 = ax1.twinx()   # USING twinx() to have the same x-axis but different y-axis, ax1,ax2,ax3
ax3 = ax1.twinx()  
rspine = ax3.spines['right']     #putting the y-axis of irradiance on the right
rspine.set_position(('axes', 1.08))    #the distance between irradiance and temperature y-axes

#plotting AC consumption
consumption_col='air conditioner_5545'      
DF_mychosenDates.plot(ax=ax1, y=consumption_col, legend=False,color='b')
ax1.set_ylabel('Consumption [W]',color='b')
ax1.tick_params(axis='y', colors='b')

#Plotting Temperature on same graph
DF_mychosenDates.plot(ax=ax2, y='temperature', legend=False, color='r')
ax2.set_ylabel('Temperature [degC]',color='r')
ax2.tick_params(axis='y',colors='r')

#plotting Irradiance on same graph
DF_mychosenDates.plot(ax=ax3,y='gen',legend=False,color='orange')
ax3.set_ylabel('Irradiance',color='orange')
ax3.tick_params(axis='y',colors='orange')

ax1.set_xlabel('Time')
plt.title("DATA FROM 1/06/14 TO 3/06/14")
plt.show()