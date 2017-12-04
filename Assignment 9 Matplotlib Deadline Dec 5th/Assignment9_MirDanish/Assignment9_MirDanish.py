import pandas as pd
import matplotlib.pyplot as plt

labels_elements = ["Wall","Roof","Door"] # Opaque Surface Elements 
columns = ["blue","red","green"] # Colors For Surfaces In Pie-Charts
HeatingLoads = [1150,1240,92]
CoolingLoads = [544,514,44]
U_old = 0.438

# Plotting Pie-charts to indicate the Heating and Cooling load percentages for each element of the opaque surfaces viz.,Wall, Roof & Door

plt.title("Heating Load For Opaque Surfaces")
plt.pie(HeatingLoads, labels = labels_elements, colors = columns, startangle = 90, explode = (0.01,0.01,0.01),autopct = '%1.1f%%')
fig1 = plt.figure()
plt.title("Cooling  Load For Opaque Surfaces")
plt.pie(CoolingLoads, labels = labels_elements,colors = columns, startangle = 90, explode = (0.01,0.01,0.01), autopct = '%1.1f%%')

# Variation Of Heating Load, By Changing The U-Value For External Wall, Shown By A 2D Plot

# Creating a range of U-Values from 0.3 to 0.6 (step = 0.05)
U_value_Series = pd.Series(range(30,60,5))*0.01 

# Creating A Function For Calculation Of Percentage Change In Heating Load Of Opaque Surfaces As Per New U-Wall Value

def percent_Change_Opaque_HeatingLoad(U_value_Series):      
    previous_heatingLoad = pd.Series(HeatingLoads).sum()
    new_heatingLoad = previous_heatingLoad*( U_value_Series/U_old)       
    return (((new_heatingLoad-previous_heatingLoad)/previous_heatingLoad)*100)
percentChange_of_Opaque_HeaingLoadSeries = U_value_Series.apply(percent_Change_Opaque_HeatingLoad)

fig2 = plt.figure()
plt.plot(U_value_Series,percentChange_of_Opaque_HeaingLoadSeries,'*',color = 'red')
plt.xlabel("U-Values For External Wall(W/m^2K)")
plt.ylabel("Overall Opaque Heating Load Percentage Change")
plt.title("Variation Of Heating Load(Opaque) wrt Change In U Of Ext. Wall") 
plt.text(0.35,20,r'$U\_old = 0.438 W/m^2K$')