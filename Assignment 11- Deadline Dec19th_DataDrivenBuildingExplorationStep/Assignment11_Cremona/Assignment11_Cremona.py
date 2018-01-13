import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = 'E:\POLIMI\MAGISTRALE\_Energy for building\Data-driven_Building_simulation_Polimi_EETBS\Data'
ConsumptionFileName = 'consumption_5545.csv'
ConsumptionFilePath = DataFolderPath+'/'+ ConsumptionFileName
DF_consumption = pd.read_csv(ConsumptionFilePath,sep=',',index_col=0)
previousIndex = DF_consumption.index
ParsedIndex = pd.to_datetime(previousIndex) 
DF_consumption.index = ParsedIndex 
DF_Dates_from_1st_to_3rd_June = DF_consumption['2014-06-01 00:00:00':'2014-06-03 23:00:00']

weatherSourceFileName = 'Austin_weather_2014.csv'
weatherSourceFilePath = DataFolderPath+'/'+ weatherSourceFileName
DF_weatherSource = pd.read_csv(weatherSourceFilePath,sep=';',index_col=0)
previousIndex1 = DF_weatherSource.index
ParsedIndex1 = pd.to_datetime(previousIndex1) 
DF_weatherSource.index = ParsedIndex1 
series_temperature = DF_weatherSource['temperature']
DF_temperature = DF_weatherSource[['temperature']] 
DF_Temperatures_from_1st_to_3rd_June = DF_temperature['2014-06-01 00:00:00':'2014-06-03 23:00:00']

IrradianceSourceFileName = 'irradiance_2014_gen.csv'
IrradianceSourceFilePath = DataFolderPath+'/'+ IrradianceSourceFileName
DF_IrradianceSource = pd.read_csv(IrradianceSourceFilePath, sep=';',index_col=1)
DF_Irradiance = DF_IrradianceSource[['gen']]
previousIndex2 = DF_IrradianceSource.index
ParsedIndex2 = pd.to_datetime(previousIndex2) 
DF_IrradianceSource.index = ParsedIndex2 
DF_Irradiance[DF_IrradianceSource['gen']<0] 
DF_Irradiance[DF_IrradianceSource['gen']<0] = 0
DF_IrrValues_from_1st_to_3rd_June = DF_Irradiance['2014-06-01 00:00:00':'2014-06-03 23:00:00']

DF_TotalData_from_1st_to_3rd_June = DF_Dates_from_1st_to_3rd_June.join([DF_Temperatures_from_1st_to_3rd_June,DF_IrrValues_from_1st_to_3rd_June])
DF_TotalData_from_1st_to_3rd_June['gen']

DF_TotalData_from_1st_to_3rd_June.plot()

# For solving the problem of the scale i search on github for a code that has to implement a function
# for changing the scale of my data
# I added to this function the possibility of changing the name of the labels 
# just putting another the request of another input list with the names that i want to add
# and changing a little bit the structure of the final for loop

def chart(d,ys,yn):

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

    for ax,y,i in zip(axes,ys,yn):
        ls=line_styles.next()
        if len(y)==1:
            col = y[0]
            cols.append(col)
            color = colors.next()
            lines.append(ax.plot(d[col],linestyle =ls,label = ys,color=color))
            ax.set_ylabel(i,color=color)
        
    
              

DF = chart(DF_TotalData_from_1st_to_3rd_June,[["temperature"],["gen"],["air conditioner_5545"]],['Temperature','Irradiance','ACconsumption'])




