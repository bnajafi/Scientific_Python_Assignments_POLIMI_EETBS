import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "C:/Users/stefy/Dropbox/fork_clone/Data-driven_Building_simulation_Polimi_EETBS/Data" 

ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath  + "/" + ConsumptionFileName
DF_consumption = pd.read_csv(ConsumptionFilePath, sep=",",index_col=0)
previousConsumptionindex = DF_consumption.index                      #sort by index object
ParsedConsumptionIndex = pd.to_datetime(previousConsumptionindex)    #change the index from object to datatime
DF_consumption.index = ParsedConsumptionIndex                        #new table with new index

WeatherFileName = "Austin_weather_2014.csv"
WeatherFilePath = DataFolderPath  + "/" + WeatherFileName
DF_weather = pd.read_csv(WeatherFilePath, sep=";",index_col=0)
previousWheaterindex = DF_weather.index           
ParsedWeatherIndex = pd.to_datetime(previousWheaterindex)    
DF_weather.index = ParsedWeatherIndex             

IrradianceFileName = "irradiance_2014_gen.csv"
IrradianceFilePath = DataFolderPath  + "/" + IrradianceFileName
DF_Irradiance = pd.read_csv(IrradianceFilePath, sep=";", index_col=1)
previousIrradianceindex = DF_Irradiance.index           
ParsedIrradianceIndex = pd.to_datetime(previousIrradianceindex)    
DF_Irradiance.index = ParsedIrradianceIndex

DF_ChoosenConsumption = (DF_consumption["2014-06-01 00:00:00" :"2014-06-03 23:00:00"])/10
DF_ChoosenTemperature = DF_weather[["temperature"]]["2014-06-01 00:00:00" :"2014-06-03 23:00:00"]
DF_ChoosenIrradiance = (DF_Irradiance[["gen"]]["2014-06-01 00:00:00" :"2014-06-03 23:00:00"])*10
DF_ChoosenIrradiance[DF_Irradiance["gen"]["2014-06-01 00:00:00" :"2014-06-03 23:00:00"] <0] = 0

DF_joined = DF_ChoosenConsumption.join([DF_ChoosenTemperature,DF_ChoosenIrradiance])

DF_joined.plot()
plt.xlabel("Time")
plt.ylabel("AC Power[daW],Irradiance(*10), Temperature[F]")
plt.title("Data for 1 - 3 June 2014")