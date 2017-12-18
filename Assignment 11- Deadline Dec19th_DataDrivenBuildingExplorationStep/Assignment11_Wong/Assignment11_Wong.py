
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "C:\Users\TOSHIBA\Documents\Italia\Building\Git\git_fork\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName 

DF_consumption = pd.read_csv(ConsumptionFilePath,sep = ",",index_col=0) 
previousIndex= DF_consumption.index
NewparsedIndex = pd.to_datetime(previousIndex)
DF_consumption.index= NewparsedIndex
DF_consumption.head(24)
DF_JulyfirstTillthird = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_JulyfirstTillthird.head(5)
DF_JulyfirstTillthird.describe()
# In[48]:



# Now let's import some weather data!
weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = DataFolderPath+"/"+weatherSourceFileName 
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep = ";",index_col=0)
DF_weatherSource.index

previousIndex_weatherSource= DF_weatherSource.index
NewparsedIndex_weatherSource = pd.to_datetime(previousIndex_weatherSource)
DF_weatherSource.index= NewparsedIndex_weatherSource

#  we usually do this
series_temperature = DF_weatherSource['temperature']

# Nut now I would prefer to have it as a dataframe with just one column, we will then see why !!
DF_temperature = DF_weatherSource[['temperature']]
# let's do the same for irradiation!!!
IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath =  DataFolderPath+"/"+IrradianceSourceFileName 
DF_irradianceSource = pd.read_csv(IrradianceSourceFilePath, sep = ";",index_col= 1)
DF_irradianceSource.head(5)

previousIndex_irradianceSource= DF_irradianceSource.index
NewparsedIndex_irradianceSource = pd.to_datetime(previousIndex_irradianceSource)
DF_irradianceSource.index= NewparsedIndex_irradianceSource

# IF I want take just the column "gen " as a dataframe with a single column !
DF_irradiance = DF_irradianceSource[["gen"]]# to take it as a DF
DF_irradiance[DF_irradianceSource["gen"] < 0] = 0

DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined.head(24)

# what to do with Nans 
DF_joined.dropna() #it will remove all Nans !!!!! 

#plt.figure()
#plt.plot(DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"])
#DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"].plot()
#plt.xlabel('Time')
#plt.ylabel('AC Power [W]')
#plt.show()

# d = Pandas Dataframe, 
# ys = [ [cols in the same y], [cols in the same y], [cols in the same y], .. ] 
def chart(d,ys):

    from itertools import cycle
    fig, ax = plt.subplots()

    axes = [ax]
    for y in ys[1:]:
        # Twin the x-axis twice to make independent y-axes.
        axes.append(ax.twinx())

    extra_ys =  len(axes[2:])

    # Make some space on the right side for the extra y-axes.
    if extra_ys>0:
        temp = 0.85
        if extra_ys<=2:
            temp = 0.75
        elif extra_ys<=4:
            temp = 0.6
        if extra_ys>5:
            print 'you are being ridiculous'
        fig.subplots_adjust(right=temp)
        right_additive = (0.98-temp)/float(extra_ys)
    # Move the last y-axis spine over to the right by x% of the width of the axes
    i = 1.
    for ax in axes[2:]:
        ax.spines['right'].set_position(('axes', 1.+right_additive*i))
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        ax.yaxis.set_major_formatter(matplotlib.ticker.OldScalarFormatter())
        i +=1.
    # To make the border of the right-most axis visible, we need to turn the frame
    # on. This hides the other plots, however, so we need to turn its fill off.

    cols = []
    lines = []
    line_styles = cycle(['-','-','-', '--', '-.', ':', '.', ',', 'o', 'v', '^', '<', '>',
               '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_'])
    colors = cycle(matplotlib.rcParams['axes.color_cycle'])
    for ax,y in zip(axes,ys):
        ls=line_styles.next()
        if len(y)==1:
            col = y[0]
            cols.append(col)
            color = colors.next()
            lines.append(ax.plot(d[col],linestyle =ls,label = col,color=color))
            ax.set_ylabel(col,color=color)
            #ax.tick_params(axis='y', colors=color)
            ax.spines['right'].set_color(color)
        else:
            for col in y:
                color = colors

fig1=chart(DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"],[["air conditioner_5545"],["temperature"],["gen"]])