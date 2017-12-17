import numpy as np
import matplotlib.pyplot as plt

heating_load_values = [1163.1,1240.0,92.5]
cooling_load_values = [550.1,514.6,43.0]
labels = ["wall","ceiling","door"]
heating_colors = ["red","orange","yellow"]
cooling_colors = ["blue","green","violet"]

# pie chart showing the share of each component in the total heating load:
plt.figure()
figure_1 = plt.pie(heating_load_values, labels = labels, colors = heating_colors, startangle = 90, explode = (0.01,0,0), autopct = '%1.1f%%')

# pie chart showing the share of each component in the total cooling load
plt.figure()
figure_2 = plt.pie(cooling_load_values, labels = labels, colors = cooling_colors, startangle = 90, explode = (0.01,0.01,0.01), autopct = '%1.1f%%')

#2D plot which shows the effect of changing only the U value of the external wall on the overall heating load
U_values_wall = np.arange(0.22,0.881,0.01)
delta_T_heating = 24.8
area_wall = 105.8
new_heating_load_values=[]
for any_U in U_values_wall:
    Q_wall_i = area_wall*any_U*delta_T_heating
    Q_tot_i=Q_wall_i+heating_load_values[1]+heating_load_values[2]
    new_heating_load_values.append(Q_tot_i)
plt.figure()
figure_3=plt.plot(U_values_wall,new_heating_load_values)
plt.xlabel("U_values_wall")
plt.ylabel("new_heating_load_values")   
plt.show(figure_3)
