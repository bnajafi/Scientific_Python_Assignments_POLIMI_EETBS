import pandas as pd,matplotlib.pyplot as plt
pd.set_option('mode.chained_assignment', None)  #---Just to supress copy warning---
FolderPath = "C:\Users\Debayan\Dropbox (Personal)\Data-driven_Building_simulation_Polimi_EETBS\Data"
#For AC consumption
FileName = "consumption_5545.csv"
FilePath = FolderPath+"/"+FileName
DF_consumptionSource= pd.read_csv(FilePath,sep = ",",index_col=0)
parsedIndex = pd.to_datetime(DF_consumptionSource.index)
DF_consumptionSource.index= parsedIndex
DF_ACconsumption = DF_consumptionSource [["air conditioner_5545"]] # Taking column "air conditioner_5545"  as a dataframe with just one column
# For ambient temperature
weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = FolderPath+"/"+weatherSourceFileName
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep = ";",index_col=0)
NewparsedIndex_weatherSource = pd.to_datetime(DF_weatherSource.index)
DF_weatherSource.index= NewparsedIndex_weatherSource
DF_ambientTemperature = DF_weatherSource[["temperature"]] # Taking column "temperature"  as a dataframe with just one column
# For irradiation
IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath =  FolderPath+"/"+IrradianceSourceFileName
DF_irradianceSource = pd.read_csv(IrradianceSourceFilePath, sep = ";",index_col= 1)
NewparsedIndex_irradianceSource = pd.to_datetime(DF_irradianceSource.index)
DF_irradianceSource.index= NewparsedIndex_irradianceSource
DF_irradiance= DF_irradianceSource[["gen"]] # Taking column "gen"  as a dataframe with just one column
DF_irradiance[DF_irradianceSource["gen"] < 0] = 0 #setting negative values to zero using index array
#Scaling Values
DF_irradiance_scaled = DF_irradiance*300
DF_ambientTemperature_scaled = DF_ambientTemperature*10
#joining
DF_joined = DF_ACconsumption.join([DF_ambientTemperature_scaled,DF_irradiance_scaled])
#Taking a particular range of dates
DF_myChosenDates = DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_myChosenDates.dropna() #drop nan values
#plotting
plt.figure()
plt.xlabel("Time------------------------>")
plt.ylabel("AC Consumption and scaled Ambient Temperature&Irrandiance(PV gen)")
plt.title("Comparaison of AC Consumption[Blue] and scaled Ambient Temperature[Yellow]&Irrandiance(PV gen)[Green] from 1st June,2014 to 3rd June,2014")
plt.plot(DF_myChosenDates)
plt.show()
