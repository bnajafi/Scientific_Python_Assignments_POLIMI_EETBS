import pandas as pd
import matplotlib.pyplot as plt

x=range(-10,11)  #makes a range of numbers--(from-10 to 10)....Excludes last number
x_series = pd.Series(x)  # Converts it to panda form

def ourFunction(x):    #def for definning functions
    y=x**2-5
    return y
    
y_series = x_series.apply(ourFunction)


x1=[1,3,5,8]
y1=[12,18,28,39]

plt.plot(x1,y1)  # to show the ploted graph

plt.xlabel("This is the name of my x axis") # gives name to the x axis
plt.ylabel("This is the name of my y axis")  # gives name to the y axis
plt.title("This is just a random useless plot!")  # gives name to the graph

x2=[2,4,7,8]
y2=[10,21,25,42]
plt.plot(x2,y2) # adds this graph to the previous one plotted 
plt.plot(x2,y2, hold=False) # shows the recent one and removes the rest

plt.close("all") # closes the graph shown
plt.plot(x_series,y_series) # the plt.plot shows the plot
plt.figure() # makes a new graph without axis

fig1 = plt.figure()
plt.close(fig1)
plt.figure(1)

plt.figure()
# How to plot scatter plots !!
x4=[3,4,5,8,12]
y4=[45,58,87,95,115]
x5=[4,5,9,10,11]
y5=[23,29,65,82,80]

plt.scatter(x4,y4,color="b",marker="*",s=50)
plt.scatter(x5,y5,color="r",marker="o",s=50)
plt.legend()
plt.close()

items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = [2500,1800,150]
cols=["r","b","g"]

plt.bar(items,HeatingLoadValues,color="g") # Shows the graph in barchart
plt.xticks(items,labels,color="r")

# How to plot a piechart
plt.close("all")
plt.figure()
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')

# RLF example 1, for the opaque surfaces changing the u values by myself