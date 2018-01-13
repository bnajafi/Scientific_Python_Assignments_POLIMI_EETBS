#Assignment 11
#Name: Shashwat Parsana

import pandas as pd
import matplotlib.pyplot as plt

Datafolderpath="G:/Sem 1/ENERGY AND ENVIRONMENTAL TECHNOLOGIES FOR BUILDING SYSTEMS/Canopy Files/Assignment 11_Parsana/Data"
consumptionfilename="consumption_5545.csv"
consumptionfilepath=Datafolderpath+"/"+consumptionfilename

DF_consumption=pd.read_csv(consumptionfilepath,sep=",",index_col=0)
previousIndex=DF_consumption.index
ParsedIndex=pd.to_datetime(previousIndex) #to convert it into proper date and time from above line program(previousIndex)
DF_consumption.index=ParsedIndex # we made it equal to parsed ,to make it into datetime format
DF_consumption.head(24)

DF_first3daysofjune=DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

#importing weather data
weatherSourceFileName="Austin_weather_2014.csv"
weatherSourceFilePath=Datafolderpath+"/"+weatherSourceFileName
DF_weatherSource=pd.read_csv(weatherSourceFilePath,sep=";",index_col=0)

previousIndex_weatherSource=DF_weatherSource.index
ParsedIndex_weatherSource=pd.to_datetime(previousIndex_weatherSource) #to convert it into proper date and time from above line program(previousIndex)
DF_weatherSource.index=ParsedIndex_weatherSource

DF_ChosenDates=DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

series_temperature=DF_weatherSource["temperature"]
DF_temeperature=DF_weatherSource[["temperature"]] 

#importing Irradiation data
IrridianceSOurceFile="irradiance_2014_gen.csv"
IrridianceFilePath=Datafolderpath+"/"+IrridianceSOurceFile
DF_IrridianceSource=pd.read_csv(IrridianceFilePath,sep=";",index_col=1)

previousIndex_IrradianceSource=DF_IrridianceSource.index
ParsedIndex_IrradianceSource=pd.to_datetime(previousIndex_IrradianceSource) #to convert it into proper date and time from above line program(previousIndex)
DF_IrridianceSource.index=ParsedIndex_IrradianceSource # we made it equal to parsed ,to make it into datetime format

DF_irradiance=DF_IrridianceSource[["gen"]]
DF_irradiance[DF_IrridianceSource["gen"]<0]=0


#Scaling tofor better comparision
DF_irradiance_scaled = DF_irradiance*300
DF_ambientTemperature_scaled = DF_temeperature*10

DF_joined=DF_consumption.join([DF_ambientTemperature_scaled,DF_irradiance_scaled]) #joining
DF_joined.dropna()

#Since I am interested in June 1st 2014 until June 3rd 2014
DF_myChosenDates=DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

#Plotting all the data in one graph
plt.figure()
plt.xlabel("Time------------------------>")
plt.ylabel("AC Consumption and scaled Temperature & Irrandiance(PV gen)")
plt.title("From 1st June,2014 to 3rd June,2014,comparaison of AC Consumption[Blue] and scaled Temperature[Yellow] & Irrandiance(PV gen) [Green]")
plt.plot(DF_myChosenDates)
plt.show()










