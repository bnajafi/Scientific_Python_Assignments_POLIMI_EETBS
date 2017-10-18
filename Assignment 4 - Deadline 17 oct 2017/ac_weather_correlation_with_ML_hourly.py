import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
from sklearn import linear_model, svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

'''====================PASTE YOUR DIRECTORY HERE=============================================='''
#==================================================================================================================
dir = 'C:/Users/MANOJ/Dropbox/Manoj Thesis/NILMTK DataSets/Pecan Street (Wiki Energy)/Exported Data From interactive Data/Building 6636' #paste your directory here 
#==================================================================================================================
os.chdir(dir)
from standard_func import standardize, pearson, pearson_withDelay, hour_data, remove_duplicates

#######Loading Dataframes from the Building Power consumption, Weather and Solar Data################
ac_data = pd.read_csv('air1+AC_hourly data.csv',sep=';')
weather = pd.read_csv('weather.csv',sep=';')
solar = pd.read_csv('solar_2013.csv',header=2)

#======================================================================================
'''======AC consumption Dataframe(Air compressor only, airwindowunit1 neglected===='''
#======================================================================================
ac_data['localminute'] =  pd.to_datetime(ac_data['localminute'], format='%d/%m/%Y %H:%M') #needs pandas 0.19
ac_consumptions = pd.DataFrame(ac_data['air1'].values, index=pd.DatetimeIndex(ac_data['localminute']), columns=['power consumption'])
ac_consumptions = remove_duplicates(ac_consumptions)
#==========================================================================================
'''================temperature DataFrame for 2013 from weather Data======================='''
#===========================================================================================
weather['localhour'] = pd.to_datetime(weather['localhour'], format='%d/%m/%Y %H:%M') #needs pandas 0.19
weather_temperatures =pd.DataFrame(weather['temperature'].values, index=(pd.DatetimeIndex(weather['localhour'])),columns=['temperature'])
start = weather_temperatures.index.searchsorted(datetime(2013, 01, 01, 0, 0, 0))
end = weather_temperatures.index.searchsorted(datetime(2014, 01, 01, 0, 0, 0))
weather_temperature_2013 = weather_temperatures.ix[start:end]
weather_temperature_2013 = remove_duplicates(weather_temperature_2013)

#=======================================================================
'''========================SOLAR DataFrame==========================='''
#=====================================================================
solar['Year'] = pd.to_datetime(solar['Year'].astype(str) + '-' + solar['Month'].astype(str) + '-' + solar['Day'].astype(str) + ' ' + solar['Hour'].astype(str) + ':' + solar['Minute'].astype(str) + ':00')
solar_DNI = pd.DataFrame(solar['Total DNI'].values, index =pd.DatetimeIndex(solar['Year']), columns=['total DNI'])
#solar_DNI=solar_DNI[6:] #[6:] so that it syncs with timeseries of temperatures & Power Consumption
solar_DNI = remove_duplicates(solar_DNI)
#==============================================================================
'''===========================Humidity ============================'''
#==============================================================================
humidity = pd.DataFrame(weather['humidity'].values, index=(pd.DatetimeIndex(weather['localhour'])),columns=['humidity'])
weather_humidity_2013 = humidity.ix[start:end]
weather_humidity_2013 = remove_duplicates(weather_humidity_2013)

#==============================================================================
'''=======================Wind Speed=============================='''
#==============================================================================
wind_speed = pd.DataFrame(solar['Wind speed (M/s)'].values, index =pd.DatetimeIndex(solar['Year']), columns=['wind speed'])
#wind_speed = wind_speed[6:] ##[6:] so that it syncs with timeseries of temperatures & Power Consumption

#==============================================================================
'''=======================Writing clean data to CSV=============================='''
#==============================================================================
data_2013 = pd.concat([weather_temperature_2013
                       ,solar_DNI,weather_humidity_2013
                       ,wind_speed,
                       ac_consumptions], axis=1)
#
#path = dir + "/complete_data.csv"
#data_2013.to_csv(path, sep=';')

########Plotting axes##########
x1 = ac_consumptions.index
x2 = weather_temperature_2013.index
x3 = solar_DNI.index
y1 = ac_consumptions.values
y2 = weather_temperature_2013.values
y3 = solar_DNI.values

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax1.twinx()
# Twin the x-axis twice to make independent y-axes.
axes = [ax1, ax2, ax3]
# Make some space on the right side for the extra y-axis.
fig.subplots_adjust(right=0.75)
# Move the last y-axis spine over to the right by 20% of the width of the axes
axes[-1].spines['right'].set_position(('axes', 1.1))
# To make the border of the right-most axis visible, we need to turn the frame
# on. This hides the other plots, however, so we need to turn its fill off.
axes[-1].set_frame_on(True)
axes[-1].patch.set_visible(False)
ax1.plot(x1, y1, 'g-')
ax2.plot(x2, y2, 'b-')
ax3.plot(x3, y3, 'r-')
ax1.set_xlabel('DATE TIME')
ax1.set_ylabel('Power Consumption in kW', color='g')
ax2.set_ylabel('Temperature in F', color='b')
ax3.set_ylabel('Direct Normal Irradiance in W/m^2', color='r')
plt.show()


std_temperature = standardize(weather_temperature_2013,'temperature')
std_ac_consumption = standardize(ac_consumptions,'power consumption')
std_DNI = standardize(solar_DNI,'total DNI')
std_humidity = standardize(weather_humidity_2013,'humidity')
std_wind_speed = standardize(wind_speed,'wind speed')
#these 5 variables are Pandas Dataframe  having days 1-365 as index 
#and hourly data as columns
#for example: std_temperature[25] is an array of hourly temperatures
#of the 25th day of 2013
#also make sure all the data starts from same hour of the same day

hourly_temperature = weather_temperature_2013.reset_index(drop=True)
hourly_ac_consumption = ac_consumptions.reset_index(drop=True)
hourly_DNI = solar_DNI.reset_index(drop=True)
hourly_humidity = weather_humidity_2013.reset_index(drop=True)
hourly_wind_speed = wind_speed.reset_index(drop=True)


#==============================================================================
'''==========Weekends list series (Weekdays = 0, Weekends = 1)======='''
#==============================================================================
weather_temperature_2013['weekend'] = weather_temperature_2013.index.dayofweek
days = {0:0,1:0,2:0,3:0,4:0,5:1,6:1}

weather_temperature_2013['weekend'] = weather_temperature_2013['weekend'].apply(lambda x: days[x])
weekends = weather_temperature_2013['weekend'].reset_index(drop=True)
#==============================================================================

a = hourly_temperature['temperature']
b = hourly_DNI['total DNI']
c = hourly_humidity['humidity']
d = hourly_wind_speed['wind speed']
e = weekends
f = hourly_ac_consumption['power consumption']

data_2013 = pd.concat([a,b,c,d,e,f], axis=1, ignore_index=False) #last column prediction feature
data_2013 = data_2013.fillna(0)
data_2013.set_index(pd.DatetimeIndex(ac_data['localminute']),drop=True,inplace=True)
""" Try to check for correlation between data, consider the lagged effect of solar
irradiance on temperature and power consumption
"""
def crosscorr(datax, datay, lag=0):
    return datax.corr(datay.shift(lag))

correlation = [crosscorr(data_2013['total DNI'], data_2013['temperature'], lag=i) for i in np.arange(-500,500,1))]
corr_array = np.array(correlation)
corr_array1 = np.nan_to_num(corr_array)
print corr_array1.max()
''' there could be a 88% correlation between temperature and DNI at a particular shift/lag level
Either ==> 88% overall correlation with DNI and temperature at a particular shift/lag
or     ==> maximum 88% correlation at a somewhere along the trend at a particular shift/lag
How do I understand and evaluate the correlation between them ?
'''


#==============DATA MODIFICATION FOR REGRESSION===================#######
array = (pd.concat([a,b,c,d,e,f], axis=1, ignore_index=False)).values
data_2013_features = array[:,0:len(data_2013.columns)-1]
data_2013_labels = (array[:,len(data_2013.columns)-1]).reshape(-1,1)

features_train, features_test, labels_train, labels_test = train_test_split(data_2013_features, data_2013_labels, test_size=0.15, random_state=42)

#=============LINEAR REGRESSION==============
regr = linear_model.LinearRegression(fit_intercept=True)
regr = regr.fit(features_train, labels_train)
acc = regr.score(features_test,labels_test)

# The coefficients
print('Coefficients: \n', regr.coef_)

# The mean squared error
print("Mean squared error: %.2f" % np.mean((regr.predict(features_test) - labels_test) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f\n\n' % regr.score(features_test, labels_test))


