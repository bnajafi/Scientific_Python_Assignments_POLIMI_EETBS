import os 
import pandas as pd
import numpy as np
os.chdir("C:\Users\Utente\Desktop\POLIMI\Polimi Lezioni\Building Systems\exercises//02-11-17")

windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
print windows_DF.columns
print windows_DF.index

windows_DF["width"]["west"]
windows_DF["Height"]["east"]

windows_DF.loc["west","width"] #alternative way of calling

windows_DF["Area"] = windows_DF["Height"]*windows_DF["width"]
windows_DF.to_csv("windows_completed1.csv",sep = ";")
windows_DF.to_html("windows_completed1.html") #to give data on a web page!

windows_IAC_cl = pd.read_csv("IAC_cl.csv",sep = ";",index_col = 1)
print windows_IAC_cl.columns
print windows_IAC_cl.index.tolist() #puts the index in a list

IAC_value = windows_IAC_cl["BlindsDark"]["5c"]

ID_intShading_eastWindow = windows_DF["IntShading_ID"]["east"]
ID_window_eastWindow = windows_DF["Window_ID"]["east"]
IAC_value_eastWindow = windows_IAC_cl[ID_intShading_eastWindow][ID_window_eastWindow]

windows_DF["IAC_cl"] = np.array([IAC_value_eastWindow,0,0,0])