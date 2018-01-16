# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:58:42 2017

@author: edoua
"""

import pandas as pd
import matplotlib.pyplot as plt

FolderPath = "C:\Users\edoua\Dropbox\Scientific_Python_Assignments_POLIMI_EETBS\Assignment 11- Deadline Dec19th_DataDrivenBuildingExplorationStep\Assignment11_Thouvenin"
ConsumptionFile = "consumption_5545.csv"
IrradianceFile = "irradiance_2014_gen.csv"
WeatherFile = "Austin_weather_2014.csv"

DF_ConsumptionSource = pd.read_csv(FolderPath+"/"+ConsumptionFile, sep=",", index_col = 0)
DF_IrradianceSource =  pd.read_csv(FolderPath+"/"+IrradianceFile, sep=";", index_col = 1)
DF_WeatherFileSource = pd.read_csv(FolderPath+"/"+WeatherFile, sep=";", index_col = 0)

DF_ConsumptionSource.index = pd.to_datetime(DF_ConsumptionSource.index)
DF_IrradianceSource.index = pd.to_datetime(DF_IrradianceSource.index)
DF_WeatherFileSource.index = pd.to_datetime(DF_WeatherFileSource.index)

DF_Consumption = DF_ConsumptionSource [["air conditioner_5545"]]
DF_Irradiance = DF_IrradianceSource [["gen"]]
DF_Irradiance[DF_IrradianceSource["gen"]<0] = 0
DF_Weather = DF_WeatherFileSource [["temperature"]]

DF_Consumption=DF_Consumption/20   #To adapt the scale

DF_Consumption = DF_Consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_Irradiance = DF_Irradiance["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_Weather = DF_Weather["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

DF_joined = DF_Consumption.join([DF_Irradiance,DF_Weather])
DF_joined.dropna()

plt.figure()
plt.plot(DF_joined)

plt.xlabel("Time")
plt.ylabel("Irrandiance, Temperature and AC Consumption/20")
plt.title("Comparaison of the Irradiance, the Temperature and the AC Consumption for a given period ")









