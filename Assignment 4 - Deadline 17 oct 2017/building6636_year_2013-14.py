# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 19:41:08 2017

@author: MANOJ
"""
''' FOR BUILDING 6636 '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#2013
path_consumption_2013 = "C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/Exported Data From interactive Data/Building 6636/knime/Energy consumption Austin/2013/6636_austin_all_appliance_2013.csv"
path_weather_2013 = "C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/Exported Data From interactive Data/Building 6636/knime/weather_austin/Austin_weather_2013.csv"
#2014
path_consumption_2014 = "C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/Exported Data From interactive Data/Building 6636/knime/Energy consumption Austin/2014/6636_austin_all_appliance_2014.csv"
path_weather_2014 = "C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/Exported Data From interactive Data/Building 6636/knime/weather_austin/Austin_weather_2014.csv"


def building_data_gen(path_consumption,path_weather):
    consumption = pd.read_csv(path_consumption,sep=';',parse_dates = {'dateTime': ['localhour']},index_col = 'dateTime')
    consumption = consumption.resample(rule='H').mean()
    #################################################
    weather = pd.read_csv(path_weather,sep=';',parse_dates = {'dateTime': ['localhour']},index_col = 'dateTime',date_parser=lambda x: pd.to_datetime(x.rpartition('-')[0]))
    weather = weather.resample(rule='H').mean()
    #####################################################
    combined = pd.concat([consumption,weather],axis='columns')
    return combined.dropna(axis='columns',how='all')    

def feature_create(df):
    df = df.resample('H').mean()
    df['hour'] = df.index.hour
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['week_of_year'] = df.index.week
    df['day_of_week'] = df.index.weekday #monday = 0 sunday = 6
    return df
    
building_2013 = building_data_gen(path_consumption_2013,path_weather_2013)
building_2014 = building_data_gen(path_consumption_2014,path_weather_2014)
building_2013_14 = pd.concat([building_2013,building_2014])

building_2013_14_features = feature_create(building_2013_14)

building_2013_14_features_daily = building_2013_14_features.resample('D').mean()



