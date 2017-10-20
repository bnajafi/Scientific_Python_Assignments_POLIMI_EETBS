# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:39:04 2017

@author: MANOJ
"""

import pandas as pd
import os

dir = 'C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/Exported Data From interactive Data/' #paste your directory here 
#==================================================================================================================
os.chdir(dir)

#######Loading Dataframes from the Building Power consumption, Weather and Solar Data################
solar = pd.read_csv('TMY_solar_2013.csv')

#=======================================================================
'''========================SOLAR DataFrame==========================='''
#=====================================================================
solar['Year'] = pd.to_datetime(solar['Year'].astype(str) + '-' + solar['Month'].astype(str) + '-' + solar['Day'].astype(str) + ' ' + solar['Hour'].astype(str) + ':' + solar['Minute'].astype(str) + ':00')
solar.set_index(['Year'],inplace=True)
solar.drop(['Month'],axis=1,inplace=True)
solar.drop(['Day'],axis=1,inplace=True)
solar.drop(['Hour'],axis=1,inplace=True)
solar.drop(['Minute'],axis=1,inplace=True)

solar_resampled = solar.resample('30T').asfreq()[0:]
solar_linear_int = solar_resampled.interpolate(method='linear', axis=0).bfill()
solar_2013 = solar_linear_int.resample('H').asfreq()[0:]
solar_2013.dropna(inplace=True)


solar_2013.to_csv('C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/Exported Data From interactive Data/TMY_DNI_temp_RH_Pressure_windSpeed_2013.csv')

