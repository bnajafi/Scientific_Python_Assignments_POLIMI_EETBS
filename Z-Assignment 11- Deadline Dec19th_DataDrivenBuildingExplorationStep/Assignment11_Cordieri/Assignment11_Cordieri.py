import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
DataFolderPath="C:\Users\SilviaAnna\Dropbox\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConsumptionFileName="consumption_5545.csv"
IrradianceFileName="irradiance_2014_gen.csv"
WeatherFileName="Austin_weather_2014.csv"

ConsumptionFilePath=DataFolderPath+"/"+ConsumptionFileName
IrradianceFilePath=DataFolderPath+"/"+IrradianceFileName
WeatherFilePath=DataFolderPath+"/"+WeatherFileName

DF_consumption=pd.read_csv(ConsumptionFilePath,sep=",",index_col=0)
previousConsumptionIndex=DF_consumption.index
NewConsumptionIndex=pd.to_datetime(previousConsumptionIndex)
DF_consumption.index=NewConsumptionIndex
DF_consumption_June2014FirstTillThird=DF_consumption["2014-06-01":"2014-06-03"]

DF_IrradianceSource=pd.read_csv(IrradianceFilePath,sep=";",index_col=1)
DF_IrradianceSource[DF_IrradianceSource["gen"]<0]=0
DF_Irradiance=DF_IrradianceSource[["gen"]]
previousIrradianceIndex=DF_Irradiance.index
NewIrradianceIndex=pd.to_datetime(previousIrradianceIndex)
DF_Irradiance.index=NewIrradianceIndex
DF_Irradiance_June2014FirstTillThird=DF_Irradiance["2014-06-01":"2014-06-03"]

DF_Weather=pd.read_csv(WeatherFilePath,sep=";",index_col=0)
previousWeatherIndex=DF_Weather.index
NewWeatherIndex=pd.to_datetime(previousWeatherIndex)
DF_Weather.index=NewWeatherIndex
DF_Weather_June2014FirstTillThird=DF_Weather["2014-06-01":"2014-06-03"]
DF_temperature_June2014FirstTillThird=DF_Weather_June2014FirstTillThird[["temperature"]]

DF_joined=DF_consumption_June2014FirstTillThird.join([DF_Irradiance_June2014FirstTillThird,DF_temperature_June2014FirstTillThird])
DF_final=DF_joined.dropna()
print DF_final
DF_final.plot()

#Correction Part
DF_Consumption1=(DF_consumption_June2014FirstTillThird)/10
DF_joined1=DF_Consumption1.join([DF_Irradiance_June2014FirstTillThird,DF_temperature_June2014FirstTillThird])
DF_joined1.plot()
plt.show()